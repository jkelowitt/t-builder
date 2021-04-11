from numpy import array, arange, divide, where, flip, abs
from numpy.core.fromnumeric import prod, sum, transpose
from pandas import DataFrame
from scipy.interpolate import InterpolatedUnivariateSpline as ius
from typing import List, Tuple, Generator, Any


def pk_to_k(pk) -> array:
    """Convert pK values to K values"""
    return array(10.0 ** (-array(pk)))


def closest_value(num: float, arr: array) -> float:
    """Returns the closest value to the number in the array."""
    return min(arr, key=lambda x: abs(x - num))


class Compound:
    def __init__(self, name: str, acidic: bool, pKas: List):
        self.name = name
        self.acidic = acidic
        self.pKas = pKas
        self.K = pk_to_k(pKas)


class AcidBase:
    def __init__(self, analyte: Compound, titrant: Compound, precision: int = 2, pKw: float = None, temp: float = None):
        self.analyte_is_acidic = analyte.acidic
        self.pk_analyte = analyte.pKas
        self.k_analyte = pk_to_k(analyte.K)
        self.titrant_acidity = titrant.acidic
        self.k_titrant = pk_to_k(titrant.K)
        self.pk_titrant = titrant.pKas

        self.aname: str = analyte.name
        self.tname: str = titrant.name

        if pKw is not None:  # If given a pKw
            self.kw = 10 ** (-pKw)
        elif temp is not None:  # If given a temperature
            self.kw = 10 ** (-self.get_kw(temp))
        else:  # If given nothing
            self.kw = 10 ** (-13.995)

        self.precision = 10 ** -precision
        self.ph, self.hydronium, self.hydroxide = self.starting_phs()

    def starting_phs(self, min_ph: float = 0, max_ph: float = 14) -> Tuple[array, array, array]:
        ph = array(arange(min_ph, max_ph + self.precision, step=self.precision))
        h = 10 ** (-ph.copy())
        oh = self.kw / h
        if self.analyte_is_acidic:
            return ph, h, oh
        else:
            return array(ph[::-1]), array(h[::-1]), array(oh[::-1])

    @staticmethod
    def get_kw(temp: float) -> float:

        # Quadratic approximation of the data for liquid water found here:
        # https://www.engineeringtoolbox.com/ionization-dissociation-autoprotolysis-constant-pKw-water-heavy-deuterium-oxide-d_2004.html
        # 0 <= T <= 95 C
        # R^2 = 0.9992
        a = 0.000128275
        b = -0.0406144
        c = 14.9368
        pKw = (a * temp ** 2) + (b * temp) + c
        return pKw


class Bjerrum(AcidBase):
    def __init__(self, analyte: Compound, titrant: Compound, precision: int, pKw: float = None, temp: float = None):

        super().__init__(analyte, titrant, precision, pKw, temp)

        self.alpha_analyte = self.alpha_values(k=analyte.K, acid=analyte.acidic)
        self.alpha_titrant = self.alpha_values(k=titrant.K, acid=titrant.acidic)

    @staticmethod
    def scale_alphas(arr: array) -> array:
        """
        Scale the alpha values by its index in the sub-array
        :param arr: Array of alpha values
        :return: The scaled alpha array
        """
        new_arr = []
        for num, a in enumerate(arr.T):
            a *= num
            new_arr.append(a)

        return array(new_arr).T

    def alpha_values(self, k: array, acid: bool = True) -> array:
        # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n , K_2 = K_w / K_(n-1)
        if not acid:
            k = self.kw / flip(k)

        # The functionality of an acid or base can be determined by the number of dissociation constants it has.
        n = len(k)

        # Get the values for the [H+]^n power
        h_vals = array([self.hydronium ** i for i in range(n, -1, -1)])

        # Get the products of the k values.
        k_vals = [prod(k[0:x]) for x in range(n + 1)]

        # Prod and Sum the h and k values
        denoms_arr = h_vals.T * k_vals  # Product of the sub-elements of the denominator
        denoms = sum(denoms_arr, axis=1)  # Sum of the sub-elements of the denominator

        # Do the outermost alpha value calculation
        alphas = divide(denoms_arr.T, denoms).T  # Divide and re-transpose

        if not acid:
            return flip(alphas, axis=0)
        else:
            return array(alphas)

    def write_alpha_data(self,
                         title: str = "Alpha Value Data",
                         file_headers: bool = False,
                         species_names: List[str] = None
                         ) -> None:

        # Initialize the dataframe with the ph values
        data_dict = {"pH": self.ph}

        # Add the alpha values for each analyte species
        if species_names is None:  # If names are not specified, just use generics.
            for num, alpha in enumerate(transpose(self.alpha_analyte)):
                data_dict[f"alpha{num}"] = alpha
        else:  # If names are specified, use them.
            for num, alpha in enumerate(transpose(self.alpha_analyte)):
                try:
                    data_dict[species_names[num]] = alpha
                except IndexError:
                    raise ValueError("You have not supplied enough species names!")

        # Make and write the data frame to a csv
        data = DataFrame(data_dict)
        data.to_csv(f"{title}.csv", index=False, header=file_headers)


class Titration(Bjerrum):
    """
    A class which defines a titration and predominance curve based on the used analyte and titrant.
    """

    def __init__(
            self,
            analyte: Compound,
            titrant: Compound,
            volume_analyte: float,
            concentration_analyte: float,
            concentration_titrant: float,
            precision: int = 2,
            pKw: float = None,
            temp: float = None,
    ):
        super().__init__(analyte, titrant, precision, pKw, temp)

        # Analyte information
        self.concentration_analyte = concentration_analyte
        self.volume_analyte = volume_analyte
        self.ka_values = analyte.K

        # Titrant Information
        self.concentration_titrant = concentration_titrant
        self.kt_values = titrant.K

        # Calculate the respective titrant values for each pH
        self.volume_titrant, self.phi = self.calculate_volume(self.titrant_acidity)

        # Trimmed values for gui plot
        self.ph_t, self.volume_titrant_t = self.trim_values(self.ph, self.volume_titrant)

    def trim_values(self, *args: Any) -> Generator:
        # Go until you are 1 past the last sub-reaction.
        limiter = len(self.k_analyte) + 1

        good_val_index = where((self.phi >= [0]) & (self.phi <= [limiter]))

        # Trim the values for every chosen data set
        rets = (arg[good_val_index] for arg in args)  # Add the trimmed dataset to the return variable

        return rets

    def calculate_volume(self, acid_titrant: bool) -> Tuple[List, List]:

        # Alpha values scaled by their index
        scaled_alphas_analyte = self.scale_alphas(self.alpha_analyte)
        scaled_alphas_titrant = self.scale_alphas(self.alpha_titrant)

        # Sum the scaled alpha values. Axis=1 forces the summation to occur for each individual [H+] value.
        summed_scaled_alphas_analyte = sum(scaled_alphas_analyte, axis=1)
        summed_scaled_alphas_titrant = sum(scaled_alphas_titrant, axis=1)

        delta = self.hydronium - self.hydroxide  # I found this written as delta somewhere, and thus it will be named.

        # Conditional addition or subtraction based on the titrant.
        if acid_titrant:
            numerator = summed_scaled_alphas_analyte + (delta / self.concentration_analyte)
            denominator = summed_scaled_alphas_titrant - (delta / self.concentration_titrant)
        else:
            numerator = summed_scaled_alphas_analyte - (delta / self.concentration_analyte)
            denominator = summed_scaled_alphas_titrant + (delta / self.concentration_titrant)

        # Solve for the volume
        phi = numerator / denominator
        volume = phi * self.volume_analyte * self.concentration_analyte / self.concentration_titrant
        return volume, phi

    def write_titration_data(self, title: str = "Titration Curve Data", file_headers: bool = False) -> None:
        # Make dataframe.
        pH, volume = self.trim_values(self.ph, self.volume_titrant)
        data = DataFrame({"volume": volume, "pH": pH})

        # Write to a csv.
        data.to_csv(f"{title}.csv", index=False, header=file_headers)

    def find_buffer_points(self) -> Tuple[List[int], array]:
        pH, volume = self.trim_values(self.ph, self.volume_titrant)
        pKas = array(self.pk_analyte)
        # All the volumes where the pH equals pKa
        volume_indices = []
        for pKa in pKas:
            places = where(pH == closest_value(pKa, pH))[0][0]
            volume_indices.append(places)

        return volume[volume_indices], pKas

    def find_equiv_points(self) -> Tuple[List, List]:
        pH, volume, phi = self.trim_values(self.ph, self.volume_titrant, self.phi)
        points = []
        for i in range(1, len(self.pk_analyte) + 1):
            closest = closest_value(i, phi)
            points.append(where(phi == closest)[0][0])

        return list(volume[points]), list(pH[points])

    def deriv(self, degree: int) -> Tuple[array, array]:
        pH, volume = self.trim_values(self.ph, self.volume_titrant)

        # An object which makes splines
        spline_maker = ius(volume, pH)

        # An object which calculates the derivative of those splines
        deriv_function = spline_maker.derivative(n=degree)

        # Calculate the derivative at all of the splines
        d = deriv_function(volume)

        return volume, d

    @staticmethod
    def _scale_data(data: array, a: float) -> array:
        """abs normalization"""
        return a * (data / (1 + abs(data)))

    def write_analysis_data(self, title: str = "Analysis Data", file_headers: bool = False) -> None:
        # Make dataframe.
        pH, volume = self.trim_values(self.ph, self.volume_titrant)
        volumeD1, deriv1 = self.deriv(1)
        volumeD2, deriv2 = self.deriv(2)
        volumeEq, pHEq = self.find_equiv_points()
        volumeBf, pHBf = self.find_buffer_points()

        analysis_row_labels = [
            *[f"eq pt {n}" for n in range(1, len(volumeEq) + 1)],
            *[f"bf pt {n}" for n in range(1, len(volumeBf) + 1)],
        ]

        analysis_volumes = [*[n for n in volumeEq], *[n for n in volumeBf]]
        analysis_pHs = [*[n for n in pHEq], *[n for n in pHBf]]

        while len(analysis_row_labels) < len(deriv1):
            analysis_row_labels.append(None)
            analysis_volumes.append(None)
            analysis_pHs.append(None)

        data = DataFrame(
            {
                "volume": volume,
                "1st Derivative": deriv1,
                "2nd Derivative": deriv2,
                " ": [" " for _ in range(len(deriv1))],
                "Analysis": analysis_row_labels,
                "Volume at Point": analysis_volumes,
                "pH at Point": analysis_pHs,
            }
        )

        # Write to a csv.
        data.to_csv(f"{title}.csv", header=file_headers, index=False)

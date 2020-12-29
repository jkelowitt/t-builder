import numpy as np
import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline as IUS


def pk_to_k(pk):
    return np.array(10. ** (- np.array(pk)))


class Compound:
    def __init__(self, name, acidic, pKs, strong):
        self.name = name
        self.acidic = acidic
        self.pKs = pKs
        self.K = pk_to_k(pKs)
        self.strong = strong


class AcidBase:
    def __init__(self, analyte, titrant, precision=0.01, pKw=None, temp=None):
        self.analyte_is_acidic = analyte.acidic
        self.pk_analyte = analyte.pKs
        self.k_analyte = pk_to_k(analyte.K)
        self.titrant_acidity = titrant.acidic
        self.k_titrant = pk_to_k(titrant.K)
        self.pk_titrant = titrant.pKs

        if pKw is not None:
            self.kw = 10 ** (-pKw)
        elif temp is not None:
            self.kw = 10 ** (-self.get_kw(temp))
        else:
            self.kw = 10 ** (-13.995)

        self.strong_analyte = analyte.strong
        self.strong_titrant = titrant.strong
        self.precision = precision
        self.ph, self.hydronium, self.hydroxide = self.starting_phs()

    def starting_phs(self, min_ph=0, max_ph=14):
        ph = np.array(np.arange(min_ph, max_ph + self.precision, step=self.precision))
        h = 10 ** (-ph.copy())
        oh = self.kw / h
        return ph, h, oh

    @staticmethod
    def get_kw(temp):
        if temp > 350 or temp < 0:
            print("Warning! The Kw calculation loses accuracy near the end of the range 0C to 350C."
                  "\nProceed with caution, or set a pKw value rather than a temperature.")

        # Variables for a quartic function found to have an R^2 > 0.9999 in Desmos.
        # This most likely works only on the range of data used: 0C to 350C
        a = 6.7179 * 10 ** -10
        b = -5.3141 * 10 ** -7
        c = 0.000199761
        d = -0.0421956
        f = 14.9376
        pKw = (a * temp ** 4) + (b * temp ** 3) + (c * temp ** 2) + (d * temp) + f
        return pKw


class Bjerrum(AcidBase):

    def __init__(self, analyte, titrant, precision=0.01, pKw=None, temp=None):

        super().__init__(analyte, titrant, precision, pKw, temp)

        self.alpha_analyte = self.alpha_values(k=analyte.K, acid=analyte.acidic)
        self.alpha_titrant = self.alpha_values(k=titrant.K, acid=titrant.acidic)

    @staticmethod
    def scale_alphas(arr):
        new_arr = []
        for item in arr:
            sub_arr = []
            for i, sub_item in enumerate(item):
                sub_item *= i
                sub_arr.append(sub_item)
            new_arr.append(sub_arr)
        new_arr = np.array(new_arr)

        return new_arr

    def alpha_values(self, k, acid=True):
        # Convert the k values to a list to help with matrix transformations.
        k = np.array(k)

        # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n , K_2 = K_w / K_(n-1)
        if not acid:
            k = self.kw / np.flip(k)

        # The functionality of an acid or base can be determined by the number of dissociation constants it has.
        n = len(k)

        # Get the values for the [H+]^n power
        powers = np.array([x for x in range(n, -1, -1)])  # List of powers
        h_vals = np.array([np.array(self.hydronium ** i) for i in powers])  # List of H values raised to the powers

        # Get the products of the k values.
        k_vals = [np.prod(k[0:x]) for x in range(n + 1)]

        # Prod and Sum the h and k values
        h_vals = h_vals.T  # Reorient the array for multiplication
        denoms_arr = np.multiply(h_vals, k_vals)  # Product of the sub-elements of the denominator
        denoms = np.sum(denoms_arr, axis=1)  # Sum of the sub-elements of the denominator

        # Do the outermost alpha value calculation
        tda = np.transpose(denoms_arr)  # Transpose the array to the correct orientation for the division
        div_arr = np.divide(tda, denoms)  # Divide
        alphas = np.transpose(div_arr)  # Re-transpose to the logically correct orientation

        if not acid:
            return np.flip(alphas, axis=0)

        return np.array(alphas)

    def write_alpha_data(self, title="Alpha Value Data", file_headers=False, species_names=None):
        # Initialize the dataframe with the ph values
        data_dict = {"pH": self.ph}

        # Add the alpha values for each analyte species
        if species_names is None:  # If names are not specified, just use generics.
            for num, alpha in enumerate(self.alpha_analyte.T):
                data_dict[f"alpha{num}"] = alpha
        else:  # If names are specified, use them.
            for num, alpha in enumerate(self.alpha_analyte.T):
                try:
                    data_dict[species_names[num]] = alpha
                except IndexError:
                    raise ValueError("You have not supplied enough species names!")

        # Make and write the data frame to a csv
        data = pd.DataFrame(data_dict)
        data.to_csv(f"{title}.csv", index=False, header=file_headers)


class Titration(Bjerrum):
    """
    A class which defines a titration and predominance curve based on the used analyte and titrant.
    """

    def __init__(self, analyte, titrant, volume_analyte, concentration_analyte, concentration_titrant, precision=0.01,
                 pKw=None, temp=None):
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
        self.ph_t, self.volume_titrant_t = self.trim_values(ph=self.ph, volume=self.volume_titrant)

    def trim_values(self, **kwargs):
        # Go until you are 1 past the last sub-reaction.
        limiter = len(self.k_analyte) + 1

        good_val_index = np.where((self.phi >= 0) & (self.phi <= limiter))

        # Trim the values for every chosen data set
        rets = (kwargs[kw][good_val_index] for kw in kwargs)  # Add the trimmed dataset to the return variable

        return rets

    def calculate_volume(self, acid_titrant):

        # Alpha values scaled by their index
        scaled_alphas_analyte = self.scale_alphas(self.alpha_analyte)
        scaled_alphas_titrant = self.scale_alphas(self.alpha_titrant)

        # Sum the scaled alpha values. Axis=1 forces the summation to occur for each individual [H+] value.
        # Since strong acids/bases fully dissociate, they only appear in their pure form, thus, their alpha values = 1
        # The alpha values are calculated to be almost exactly 1 anyways, but letting it calculate as normal breaks the
        #  calculation
        if self.strong_analyte:
            summed_scaled_alphas_analyte = np.array([1])
        else:
            summed_scaled_alphas_analyte = np.sum(scaled_alphas_analyte, axis=1)

        if self.strong_titrant:
            summed_scaled_alphas_titrant = np.array([1])
        else:
            summed_scaled_alphas_titrant = np.sum(scaled_alphas_titrant, axis=1)

        beta = self.hydronium - self.hydroxide  # No technical definition

        # Conditional addition or subtraction based on the titrant.
        if acid_titrant:
            numerator = summed_scaled_alphas_analyte + (beta / self.concentration_analyte)
            denominator = summed_scaled_alphas_titrant - (beta / self.concentration_titrant)
        else:
            numerator = summed_scaled_alphas_analyte - (beta / self.concentration_analyte)
            denominator = summed_scaled_alphas_titrant + (beta / self.concentration_titrant)

        # Solve for the volume
        phi = numerator / denominator
        volume = phi * self.volume_analyte * self.concentration_analyte / self.concentration_titrant
        return volume, phi

    def write_titration_data(self, title="Titration Curve Data", file_headers=False):
        # Make dataframe.
        pH, volume = self.trim_values(ph=self.ph, volume=self.volume_titrant)
        data = pd.DataFrame({"volume": volume,
                             "pH": pH})

        # Write to a csv.
        data.to_csv(f"{title}.csv", index=False, header=file_headers)

    def find_buffer_points(self):
        pH, volume = self.trim_values(ph=self.ph, volume=self.volume_titrant)
        pKas = np.array(self.pk_analyte)
        # All the volumes where the pH equals pKa
        volume_indices = []
        for pKa in pKas:
            try:
                volume_indices.append(np.where(pH == pKa)[0][0])
            except IndexError:
                pass

        return volume[volume_indices], pKas

    def find_equiv_points(self):
        pH, volume, phi = self.trim_values(ph=self.ph, volume=self.volume_titrant, phi=self.phi)
        points = []
        for i in range(1, len(self.pk_analyte) + 1):
            closest_value = min(phi, key=lambda x: abs(x - i))
            points.append(np.where(phi == closest_value)[0][0])

        return volume[points], pH[points]

    def deriv(self, degree):
        pH, volume = self.trim_values(pH=self.ph, volume=self.volume_titrant)

        # An object which makes splines
        spline_maker = IUS(volume, pH)

        # An object which calculates the derivative of those splines
        deriv_function = spline_maker.derivative(n=degree)

        # Calculate the derivative at all of the splines
        d = deriv_function(volume)

        return volume, d

    @staticmethod
    def scale_data(data, a):

        # """Linear Scale"""
        # return data * a

        # """See min-max feature scaling for where this equation came from"""
        # return a + ((data - np.average(data)) * (a)) / (max(data) - min(data))

        """Sigmoid scaling"""
        ee = np.e ** data
        return a * (ee / (ee + 1))

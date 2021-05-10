"""
@title: titration_class.py
@author: Jackson Elowitt

This file can be used to simulate titration curves.

First, use the Compound class to create a titrant and an analyte.

Second, pass in the analyte and titrant to the Titration class,
    along with the concentrations and volumes of the analyte and titrants.

From the titration class, call Titration.ph to obtain the trimmed pH values, and call
    Titration.volume_titrant to obtain the volume of titrant required to reach those pH values.
"""

from dataclasses import dataclass, field
from typing import List, Tuple, Generator, Any

import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as IUS


def pk_to_k(pk) -> np.array:
    """Convert pK values to K values"""
    return np.array(10.0 ** (-np.array(pk)))


def closest_value(num: float, arr: np.array) -> float:
    """Returns the closest value to the number in the array."""
    return min(arr, key=lambda x: np.abs(x - num))


@dataclass
class Compound:
    """
    Main class used to contain information about a specific compound

    Parameters
    ----------
    name : A string which holds the name of the compound
    acidic : A boolean which represents whether or not the compound is acidic. True --> Acidic, False -> Basic
    pKas: A list of floats which represents the pKa values of the compound.

    Example
    -------
    >>> analyte = Compound("Acidic Analyte", acidic=True, pKas=[3, 6, 9])
    >>> analyte.name
    'Acidic Analyte'
    >>> analyte.acidic
    True
    >>> analyte.pKas
    [3, 6, 9]
    >>> analyte.ks
    array([1.e-03, 1.e-06, 1.e-09])

    """

    name: str
    acidic: bool
    pKas: list[float]

    def __post_init__(self):
        # The k values can become zero if the pKa value is too large ~> 330.
        try:
            self.ks: np.array = np.array(10.0 ** (-np.array(self.pKas)))
        except RuntimeWarning:
            raise OverflowError("The pKa entered is very extreme. This will most likely cause problems.\
             Try a value with a magnitude less than 300.")


@dataclass
class Titration:
    """
    Main Titration Class. Performs the titration of an analyte with a titrant
        given their concentrations and volumes.

    Parameters
    ----------

    analyte : A Compound class which represents the analyte of the titration
    titrant : A Compound class which represents the titrant of the titration
    concentration_analyte : A float which represents the concentration of the analyte
    concentration_titrant : A float which represents the concentration of the titrant
    volume_analyte : A float which represents the volume of analyte being titrated

    Optional Parameters
    -------------------
    pKw : A custom value for the pKw of water. Default is None.
    temp : A custom temperature for the temperature for the titration to take place.
            Default is 25C. If pKw is None, this value is used to calculate the pKw at 25C.
    decimal_places : The number of decimal places the titration should be simulated to. Default is 2 (2 -> 0.01).

    Example
    -------
    # Make the compounds
    >>> analyte = Compound("Acidic Analyte", acidic=True, pKas=[3, 6, 9])

    >>> titrant = Compound("Basic Analyte", acidic=False, pKas=[15])

    # 'Perform' titration
    >>> titr = Titration(analyte, titrant, concentration_analyte=0.1, concentration_titrant=0.1, volume_analyte=25)

    # Extract information about the titration
    >>> titr.ph
    array([ 2.03,  2.04,  2.05, ..., 12.28, 12.29, 12.3 ])

    >>> titr.volume_titrant
    array([7.94800512e-02, 1.74868902e-01, 2.70378281e-01, ..., 9.84186264e+01, 9.90963992e+01, 9.97976880e+01])


    """

    analyte: Compound
    titrant: Compound

    concentration_analyte: float
    concentration_titrant: float

    volume_analyte: float

    pKw: float = field(default=None)
    temp: float = field(default=25)
    decimal_places: int = field(default=2)

    def __post_init__(self):
        """Important values to calculate after the initialization"""
        # Calculate the pKw
        if self.pKw is not None:  # If given a pKw
            self.kw = 10 ** (-self.pKw)
        else:  # If given a temperature
            self.kw = 10 ** (-self.temp_kw(self.temp))

        # The increment level for the value ranges
        self.precision: int = 10 ** -self.decimal_places

        # Value ranges
        self.ph_full, self.hydronium_full, self.hydroxide_full = self.starting_phs()

        # Calculate the alpha values for the compounds at each pH
        self.alpha_analyte = self.alpha_values(k=self.analyte.ks, acid=self.analyte.acidic)
        self.alpha_titrant = self.alpha_values(k=self.titrant.ks, acid=self.titrant.acidic)

        # Calculate and trim the volumes.
        self.volume_titrant_full, self.phi = self.calculate_volume(self.titrant.acidic)
        self.ph, self.volume_titrant = self.trim_values(self.ph_full, self.volume_titrant_full)

    def starting_phs(self, min_ph: float = None, max_ph: float = None) -> Tuple[np.array, np.array, np.array]:
        """Returns a range of pH, hydronium_full concentration, and hydroxide_full concentrations"""

        if min_ph is None:
            min_ph = (14 * (not self.analyte.acidic)) - np.log10(self.concentration_analyte)

        if max_ph is None:
            max_ph = (14 * (not self.titrant.acidic)) - np.log10(self.concentration_analyte)

        if self.analyte.acidic:
            ph = np.arange(min_ph, max_ph, self.precision)
        else:  # Swap max and min pH so that the proper volume order is preserved.
            ph = np.arange(max_ph, min_ph, self.precision)

        h = 10 ** (-ph)
        oh = self.kw / h
        return ph, h, oh

    @staticmethod
    def temp_kw(temp: float) -> float:
        """Returns the pKw of water given a certain temperature in celsius."""

        # Quadratic approximation of the data for liquid water found here:
        # https://www.engineeringtoolbox.com/ionization-dissociation-autoprotolysis-constant-pKw-water-heavy-deuterium-oxide-d_2004.html
        # 0 <= T <= 95 C
        # R^2 = 0.9992
        a = 0.000128275
        b = -0.0406144
        c = 14.9368
        pKw = (a * temp ** 2) + (b * temp) + c
        return pKw

    @staticmethod
    def _scale_data(data: np.array, a: float) -> np.array:
        """abs normalization"""
        return a * (data / (1 + np.abs(data)))

    @staticmethod
    def scale_alphas(arr: np.array) -> np.array:
        """Scale the alpha values by its index in the sub-array"""
        new_arr = []
        for num, a in enumerate(np.transpose(arr)):
            a *= num
            new_arr.append(a)

        return np.transpose(np.array(new_arr))

    def alpha_values(self, k: np.array, acid: bool = True) -> np.array:
        """Finds the fraction of solution which each species of compound takes up at each pH."""
        # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n , K_2 = K_w / K_(n-1)
        try:
            if not acid:
                k = self.kw / np.flip(k)
        except ZeroDivisionError:
            raise ZeroDivisionError("The pKa entered is too extreme. Try a value with a magnitude less than 300.")

        # The functionality of an acid or base can be determined by the number of dissociation constants it has.
        n = len(k)

        # Get the values for the [H+]^n power
        h_vals = np.array([self.hydronium_full ** i for i in range(n, -1, -1)])

        # Get the products of the k values.
        k_vals = [np.prod(k[0:x]) for x in range(n + 1)]

        # Prod and Sum the h and k values
        denoms_arr = np.transpose(h_vals) * k_vals  # Product of the sub-elements of the denominator
        denoms = np.sum(denoms_arr, axis=1)  # Sum of the sub-elements of the denominator

        # Do the outermost alpha value calculation
        alphas = np.transpose(np.divide(np.transpose(denoms_arr), denoms))  # Divide and re-transpose

        if acid:
            return np.array(alphas)

        return np.flip(alphas, axis=0)

    def trim_values(self, *args: Any) -> Generator:
        """Returns the data ranges where the volume is non-trivial and non-absurd."""
        # Go until you are 1 past the last sub-reaction.
        limiter = len(self.analyte.pKas) + 1

        good_val_index = np.where((self.phi >= [0]) & (self.phi <= [limiter]))

        # Trim the values for every chosen data set
        rets = (arg[good_val_index] for arg in args)  # Add the trimmed dataset to the return variable

        return rets

    def calculate_volume(self, acid_titrant: bool) -> Tuple[List, List]:
        """Calculate the volume of titrant required to reach each pH value."""
        # Alpha values scaled by their index
        scaled_alphas_analyte = self.scale_alphas(self.alpha_analyte)
        scaled_alphas_titrant = self.scale_alphas(self.alpha_titrant)

        # Sum the scaled alpha values. Axis=1 forces the summation to occur for each individual [H+] value.
        summed_scaled_alphas_analyte = np.sum(scaled_alphas_analyte, axis=1)
        summed_scaled_alphas_titrant = np.sum(scaled_alphas_titrant, axis=1)

        # I found this written as delta somewhere, and thus it will be named.
        delta = self.hydronium_full - self.hydroxide_full

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

    def find_buffer_points(self) -> Tuple[List[int], np.array]:
        """Find the volumes of the buffer points based on the pKa values."""
        pH, volume = self.trim_values(self.ph_full, self.volume_titrant_full)
        pKas = np.array(self.analyte.pKas)

        # All the volumes where the pH equals pKa
        volume_indices = []
        for pKa in pKas:
            if pKa > 14:  # Should never be larger than 14
                continue
            places = np.where(pH == closest_value(pKa, pH))[0][0]
            volume_indices.append(places)

        return volume[volume_indices], pKas

    def find_equiv_points(self) -> Tuple[List, List]:
        """Find the equivalence points based on the progression of the reaction."""
        pH, volume, phi = self.trim_values(self.ph_full, self.volume_titrant_full, self.phi)
        points = []
        for i in range(1, len(self.analyte.pKas) + 1):
            closest = closest_value(i, phi)
            points.append(np.where(phi == closest)[0][0])

        return list(volume[points]), list(pH[points])

    def deriv(self, degree: int) -> Tuple[np.array, np.array]:
        """Find the n-th derivative"""
        pH, volume = self.trim_values(self.ph_full, self.volume_titrant_full)

        # An object which makes splines
        spline_maker = IUS(volume, pH)

        # An object which calculates the derivative of those splines
        deriv_function = spline_maker.derivative(n=degree)

        # Calculate the derivative at all of the splines
        d = deriv_function(volume)

        return volume, d

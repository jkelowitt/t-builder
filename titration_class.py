"""
I'm not super great with classes, but we'll see how this goes.
"""
import numpy as np
import matplotlib.pyplot as plt

import pretty_errors


def equiv_volume(c1, v1, c2):
    """Returns the equivalence volume"""
    c1 = float(c1)
    v1 = float(v1)
    c2 = float(c2)

    return c1 * v1 / c2


def pk_to_k(pk):
    """Converts a pk, or an array or pk's to a k or an array of k's"""
    return np.array(10. ** - np.array(pk))


def scale_alphas(arr):
    """Scale every value in the sublist of the array by its index."""
    # TODO make this less horrible
    new_arr = []
    for item in arr:
        sub_arr = []
        for i, sub_item in enumerate(item):
            sub_item *= i
            sub_arr.append(sub_item)
        new_arr.append(sub_arr)
    new_arr = np.array(new_arr)
    if new_arr[0][-1] == 0:
        return np.array([[1]])
    else:
        return new_arr


class Titration:

    def __init__(self,
                 analyte_is_acidic,
                 titrant_is_acidic,
                 volume_analyte,
                 concentration_analyte,
                 concentration_titrant,
                 pkt_values,
                 pka_values,
                 kw=1.023 * (10 ** -14)  # Assuming 25C
                 ):

        # General Information
        self.kw = kw
        self.ph, self.hydronium, self.hydroxide = self.starting_phs()

        # Analyte information
        self.analyte_acidity = analyte_is_acidic
        self.concentration_analyte = concentration_analyte
        self.volume_analyte = volume_analyte
        self.pka_values = pka_values

        # Titrant Information
        self.titrant_acidity = titrant_is_acidic
        self.concentration_titrant = concentration_titrant
        self.pkt_values = pkt_values

        # Convert from pk values to k values.
        self.k_analyte = pk_to_k(self.pka_values)
        self.k_titrant = pk_to_k(self.pkt_values)

        # Calculate alpha values
        # TODO check that the inputs to this alpha value function requires hydroxide all the time, rather than
        #  if it is just an acid / base.
        self.alpha_analyte = self.alpha_values(self.k_analyte, self.hydronium)
        self.alpha_titrant = self.alpha_values(self.k_titrant, self.hydronium)

        self.volume_titrant, self.phi = self.volume_calculator(self.titrant_acidity)

        self.check_vals()

    def check_vals(self):
        """
        Find only the useful data.
        """

        limiter = len(self.pka_values)

        good_val_index = np.where((self.phi >= 0) & (self.phi <= limiter + 1))

        self.volume_titrant = self.volume_titrant[good_val_index]
        self.ph = self.ph[good_val_index]
        self.hydronium = self.hydronium[good_val_index]
        self.hydroxide = self.hydroxide[good_val_index]

        # Trim the alpha_analyte values
        try:  # If the analyte is strong, there should be no alpha values
            self.alpha_analyte = []
            for key in self.alpha_analyte:
                key = int(key)
                self.alpha_analyte[key] = self.alpha_analyte[key].astype("object")
                new_list = np.insert(self.alpha_analyte[key][good_val_index], 0, key)
                self.alpha_analyte.append(new_list)

            self.alpha_analyte = np.array(self.alpha_analyte, dtype="object")
            self.alpha_analyte = np.transpose(self.alpha_analyte)
        except:
            self.alpha_analyte = [[1]]

        # Trim the alpha_titrant values
        try:  # If the titrant is strong, there should be no alpha values
            self.alpha_titrant = []
            for key in self.alpha_titrant:
                key = int(key)
                self.alpha_titrant[key] = self.alpha_titrant[key].astype("object")
                new_list = np.insert(self.alpha_titrant[key][good_val_index], 0, key)
                self.alpha_titrant.append(new_list)
        except:
            self.alpha_titrant = [[1]]

        self.alpha_titrant = np.array(self.alpha_titrant, dtype="object")
        self.alpha_titrant = np.transpose(self.alpha_titrant)

    def starting_phs(self, min_ph=0, max_ph=14, precision=0.001):
        """Generate pH, [H+], and [OH-] lists"""
        # pH
        ph = np.array(np.arange(min_ph, max_ph + precision, step=precision))
        ph = ph.round(decimals=3)

        # Hydroxide and Hydronium
        h = 10 ** (-ph.copy())
        oh = self.kw / h
        return ph, h, oh

    def alpha_values(self, k, h, base=False, strong=False):
        """
        For a given list of K values, and a list of hydronium concentrations,
        return a list of the alpha values for every level of protonation for the analyte.

        Parameters:
            k: A list of values for k. --> [k1, k2,..., kn]
            h: A list of hydronium concentrations. --> [h_1, h_2, ..., h_m]
            base: If the solution is a base, the k values need to be converted from Kb to Ka for these calculations.
            strong: If the solution is a strong acid or base, there are no alpha values to be calculated
        """
        if strong:
            return np.array([[1]])

        # Convert lists to numpy arrays for easier math
        h = np.array(h)
        k = np.array(k)

        # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n , K_2 = K_w / K_(n-1)
        if base:
            k = self.kw / np.flip(k)

        # The functionality of an acid or base can be determined by the number of dissociation constants it has.
        n = len(k)

        # Get the values for the [H+]^n power
        powers = [x for x in range(n, -1, -1)]  # List of powers
        h_vals = [np.array(h ** i) for i in powers]  # List of H values raised to the powers

        # Get the scalar factors which depend solely on the k values
        k_vals = [np.prod(k[0:x]) if k.size > 0 else [1] for x in range(n + 1)]

        # Prod and Sum the h and k values
        h_vals = np.transpose(h_vals)  # Reorient the array for multiplication
        denoms_arr = np.multiply(h_vals, k_vals)  # Product of the sub-elements of the denominator
        denoms = np.sum(denoms_arr, axis=1)  # Sum of the sub-elements of the denominator

        # Do the outermost alpha value calculation
        tda = np.transpose(denoms_arr)  # Transpose the array to the correct orientation for the division
        div_arr = np.divide(tda, denoms)  # Divide
        alphas = np.transpose(div_arr)  # Re-transpose to the logically correct orientation

        if base:
            return np.flip(alphas, axis=0)
            # return alphas

        return np.array(alphas)

    def volume_calculator(self, acid_titrant):
        """
        Take in a whole bunch of information, returns a list of volumes for the given data, with a length equal to the
        [H+] and [OH-] lists.

        :param acid_titrant: Whether or not the titrant is an acid.

        :return vol: An array of volumes for the given [H+] and [OH-]
        :return phi: An array of phi (fraction of the way to the equivalence point) values
        """

        # Alpha values scaled by their index
        scaled_alphas_analyte = scale_alphas(self.alpha_analyte)
        scaled_alphas_titrant = scale_alphas(self.alpha_titrant)

        # Sum the scaled alpha values. Axis=1 forces the summation to occur for each individual [H+] value.
        summed_scaled_alphas_analyte = np.sum(scaled_alphas_analyte, axis=1)
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

    def plot_titration_curve(self):
        self.volume_calculator(self.titrant_acidity)

        if self.volume_titrant is not None and self.ph is not None:
            plt.plot(self.volume_titrant, self.ph)
            plt.show()


# Strong Trifunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
# Poly-protic basic analyte causes problems.
a = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 6, 9],
              pkt_values=[1000])

a.plot_titration_curve()

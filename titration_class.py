import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import pretty_errors

# TODO figure out why strong-strong is giving two straight lines instead of a perfect cross

class Titration:

    def __init__(self,
                 analyte_is_acidic,
                 titrant_is_acidic,
                 volume_analyte,
                 concentration_analyte,
                 concentration_titrant,
                 pkt_values,
                 pka_values,
                 strong_analyte=True,
                 strong_titrant=True,
                 title="Titration Curve",
                 precision=0.01,
                 kw=1.023 * (10 ** -14),  # Assuming 25C
                 ):

        # General Information
        self.kw = kw
        self.precision = precision
        self.ph, self.hydronium, self.hydroxide = self.starting_phs()
        self.title = title

        # Analyte information
        self.analyte_acidity = analyte_is_acidic
        self.concentration_analyte = concentration_analyte
        self.volume_analyte = volume_analyte
        self.pka_values = pka_values
        self.strong_analyte = strong_analyte

        # Titrant Information
        self.titrant_acidity = titrant_is_acidic
        self.concentration_titrant = concentration_titrant
        self.pkt_values = pkt_values
        self.strong_titrant = strong_titrant

        # Convert from pk values to k values.
        self.k_analyte = self.pk_to_k(self.pka_values)
        self.k_titrant = self.pk_to_k(self.pkt_values)

        self.alpha_analyte = self.alpha_values(k=self.k_analyte, h=self.hydronium, acid=analyte_is_acidic)
        self.alpha_titrant = self.alpha_values(k=self.k_titrant, h=self.hydronium, acid=titrant_is_acidic)

        # Calculate the respective titrant values for each pH
        self.volume_titrant, self.phi = self.volume_calculator(self.titrant_acidity)

        # Remove values from indices where the volume is negative or extremely large.
        self.check_values()

    @staticmethod
    def pk_to_k(pk):
        """Converts a pk, or an array or pk's to a k or an array of k's"""
        k = np.array(10. ** (- np.array(pk)))
        return k

    def check_values(self):
        """Find only the useful data."""

        # Go until you are 1 past the last sub-reaction.
        limiter = len(self.pka_values) + 1

        good_val_index = np.where((self.volume_titrant >= 0) & (self.phi <= limiter))

        # Cut the bad data out of each dataset.
        self.volume_titrant = self.volume_titrant[good_val_index]
        self.ph = self.ph[good_val_index]
        self.hydronium = self.hydronium[good_val_index]
        self.hydroxide = self.hydroxide[good_val_index]

        # Trim the alpha_analyte values
        new_alphas = []
        for alphas in self.alpha_analyte.T:
            new_alphas.append(alphas[good_val_index])
        self.alpha_analyte = new_alphas

        self.alpha_analyte = np.array(self.alpha_analyte, dtype="object")
        self.alpha_analyte = np.transpose(self.alpha_analyte)

        # Trim the alpha_titrant values
        new_alphas = []
        for alphas in self.alpha_titrant.T:
            new_alphas.append(alphas[good_val_index])
        self.alpha_titrant = new_alphas

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

    @staticmethod
    def scale_alphas(arr):
        # TODO make this less horrible
        new_arr = []
        for item in arr:
            sub_arr = []
            for i, sub_item in enumerate(item):
                sub_item *= i
                sub_arr.append(sub_item)
            new_arr.append(sub_arr)
        new_arr = np.array(new_arr)

        return new_arr


    def alpha_values(self, k, h, acid=True):

        # Convert lists to numpy arrays for easier math
        h = np.array(h)
        k = np.array(k)

        # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n , K_2 = K_w / K_(n-1)
        if not acid:
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

        if not acid:
            return np.flip(alphas, axis=0)

        return np.array(alphas)

    def volume_calculator(self, acid_titrant):

        # Alpha values scaled by their index
        scaled_alphas_analyte = self.scale_alphas(self.alpha_analyte)
        scaled_alphas_titrant = self.scale_alphas(self.alpha_titrant)

        # Sum the scaled alpha values. Axis=1 forces the summation to occur for each individual [H+] value.
        # Since strong acids/bases fully dissociate, they only appear in their pure form, thus, their alpha values = 1
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

    def plot_titration_curve(self):

        plt.plot(self.volume_titrant, self.ph)
        plt.title("Titration curve for\n" + self.title)
        plt.show()

    def plot_alpha_curve(self):

        plt.plot(self.ph, self.alpha_analyte)
        plt.title("Alpha Values for\n" + self.title)
        plt.show()

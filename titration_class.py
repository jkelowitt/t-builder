import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Titration:
    """
    A class which defines a titration and predominance curve based on the used analyte and titrant.
    """

    def __init__(self,
                 analyte_is_acidic,
                 volume_analyte,
                 concentration_analyte,
                 concentration_titrant,
                 pkt_values,
                 pka_values,
                 strong_analyte=True,
                 strong_titrant=True,
                 precision=0.01,
                 kw=1.023 * (10 ** -14)
                 ):
        """
        :param analyte_is_acidic:
            Whether or not the analyte is acting as acidic.
        :param volume_analyte:
            The volume of the analyte in chosen units.
        :param concentration_analyte:
            Concentration of the analyte in chosen units.
        :param concentration_titrant:
            Concentration of the titrant in chosen units.
        :param pkt_values:
            pK values for the titrant. If the titrant is acidic, use the pKa values, else use the pKb values.
        :param pka_values:
            pK values for the analyte. If the analyte is acidic, use the pKa values, else use the pKb values.
        :param strong_analyte:
            Whether or not the analyte is a strong one. Typically, pK values <-1.74 are strong in aqueous solution.
        :param strong_titrant:
            Whether or not the titrant is a strong one. Typically, pK values <-1.74 are strong in aqueous solution.
        :param precision:
            The precision to calculate the titration/alpha at. Defaults to a step size of 0.01 pH.
        :param kw:
            The dissociation constant of water. Defaults to the constant at 25 C.
        """

        # General Information
        self.kw = kw
        self.precision = precision
        self.ph, self.hydronium, self.hydroxide = self.starting_phs()

        # Analyte information
        self.analyte_acidity = analyte_is_acidic
        self.concentration_analyte = concentration_analyte
        self.volume_analyte = volume_analyte
        self.pka_values = pka_values
        self.strong_analyte = strong_analyte

        # Titrant Information
        self.titrant_acidity = not analyte_is_acidic  # The titrant is the opposite acidity as the analyte.
        self.concentration_titrant = concentration_titrant
        self.pkt_values = pkt_values
        self.strong_titrant = strong_titrant

        # Convert from pk values to k values.
        self.k_analyte = self.pk_to_k(self.pka_values)
        self.k_titrant = self.pk_to_k(self.pkt_values)

        self.alpha_analyte = self.alpha_values(k=self.k_analyte, h=self.hydronium, acid=self.analyte_acidity)
        self.alpha_titrant = self.alpha_values(k=self.k_titrant, h=self.hydronium, acid=self.titrant_acidity)

        # Calculate the respective titrant values for each pH
        self.volume_titrant, self.phi = self.volume_calculator(self.titrant_acidity)

        # Calculate the trimmed values for titration plotting. This prevents data destruction.
        self.volume_titrant_t, self.ph_t, self.hydronium_t, self.hydroxide_t, self.alpha_titrant_t, self.alpha_analyte_t = self.check_values()

    @staticmethod
    def pk_to_k(pk):
        """
        Converts a pk, or an array or pk's to a k or an array of k's

        :param pk:
            A or a list of pK values for a compound.
        :return:
            An array of the pk values respective k values in order.

        """
        k = np.array(10. ** (- np.array(pk)))
        return k

    def check_values(self):
        """
        Returns the class data trimmed to only be within a certain titration completion range.
        If a phi value of 1 represents a volume 100% of the way to the equivalence point, then a value of 2 should show
            the whole equivalence point and the end of the curve. Thus, the range we wish to show should always have a
            phi value of one more than the number of equivalence points.

        :return:
        volume_titrant, ph, hydronium, hydroxide, alpha_titrant, alpha_analyte, all trimmed to be within the
            specified range.
        """

        # Go until you are 1 past the last sub-reaction.
        limiter = len(self.pka_values) + 1

        good_val_index = np.where((self.phi >= 0) & (self.phi <= limiter))

        # Cut the bad data out of each dataset.
        volume_titrant = self.volume_titrant[good_val_index]
        ph = self.ph[good_val_index]
        hydronium = self.hydronium[good_val_index]
        hydroxide = self.hydroxide[good_val_index]

        # Trim the alpha_analyte values
        new_alphas = []
        for alphas in self.alpha_analyte.T:
            new_alphas.append(alphas[good_val_index])
        alpha_analyte = np.array(new_alphas).T

        # Trim the alpha_titrant values
        new_alphas = []
        for alphas in self.alpha_titrant.T:
            new_alphas.append(alphas[good_val_index])
        alpha_titrant = np.array(new_alphas).T

        return volume_titrant, ph, hydronium, hydroxide, alpha_titrant, alpha_analyte

    def starting_phs(self, min_ph=0, max_ph=14):
        """
        Creates a starting range of pH, hydronium, and hydroxide values.
        :param min_ph:
            The minimum value of pH to calculate from.
        :param max_ph:
            The maximum value of pH to calculate from.
        :return: ph, h, oh
            pH, hydronium concentration, and hydroxide concentration.
        """
        # pH
        ph = np.array(np.arange(min_ph, max_ph + self.precision, step=self.precision))

        # Hydroxide and Hydronium
        h = 10 ** (-ph.copy())
        oh = self.kw / h
        return ph, h, oh

    @staticmethod
    def scale_alphas(arr):
        """
        Scales each sub array by its index in the parent array.
        :param arr:
            Array to be scaled
        :return: new_arr
            Array which has been scaled.
        """
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
        """
        Calculates the alpha values for the given compound.
        :param k:
            A list of k values for the
        :param h:
            A list of hydronium concentrations.
        :param acid:
            Whether or not the compound is acidic.
        :return:
            A numpy array of alpha values for the compound.
        """

        # Convert lists to numpy arrays for easier math
        h = np.array(h)
        k = np.array(k)

        # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n , K_2 = K_w / K_(n-1)
        if not acid:
            k = self.kw / np.flip(k)

        # The functionality of an acid or base can be determined by the number of dissociation constants it has.
        n = len(k)

        # Get the values for the [H+]^n power
        powers = np.array([x for x in range(n, -1, -1)])  # List of powers
        h_vals = np.array([np.array(h ** i) for i in powers])  # List of H values raised to the powers

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

    def volume_calculator(self, acid_titrant):
        """
        Calculates the volume of titrant for each pH for the titrant and analyte.
        :param acid_titrant:
            Whether or not the titrant is an acid.
        :return: volume, phi
            The volume and reaction progress.
        """

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

    def plot_titration_curve(self, title):
        """
        Plots a titration curve for the current analyte and titrant at the trimmed pH values
        :param title:
            Title for the plot.
        :return:
            None
        """
        # Remove values from indices where the volume is negative or extremely large.
        self.check_values()

        plt.plot(self.volume_titrant_t, self.ph_t)
        plt.title(title)
        plt.show()

    def plot_alpha_curve(self, title):
        """
        Plots a bjerrum curve for the current analyte at all pH values.
        :param title:
            Title for the plot.
        :return:
            None
        """
        plt.plot(self.ph, self.alpha_analyte)
        plt.title(title)
        plt.show()

    def write_titration_data(self, title, file_headers=False):
        """
        Write to a csv file, the volume of titrant and pH at each addition.
        :param title:
            Title for the csv
        :param file_headers:
            Whether or not to include headers in the csv file.
        :return:
            None
        """
        # Make dataframe.
        data = pd.DataFrame({"volume": self.volume_titrant_t,
                             "pH": self.ph_t})

        # Write to a csv.
        data.to_csv(f"{title}.csv", index=False, header=file_headers)

    def write_alpha_data(self, title, file_headers=False, species_names=None):
        """
        Write to a csv file, the pH and ampholyte prevalence for each species in solution.
        :param title:
            Title for the csv
        :param file_headers:
            Whether or not to include headers in the csv file.
        :param species_names:
            Ordered names for each of the ampholyte species.
        :return:
            None
        """
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

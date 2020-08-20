"""
All general use functions in the program. Used Basically everywhere.
"""

import numpy as np

kw = 1.023 * (10 ** -14)  # At 25 degrees celsius


def check_vals(vol, ph, h, oh, phi, pka_vals, aanalyte, atitrant):
    """
    Find only the useful data.
    :param vol: A list of volumes
    :param ph: A list of pH's
    :param h: A list of hydroniums
    :param oh: A list of hydroxides
    :param phi: A list of phi values
    :param pka_vals: A list of pK values for the analyte
    :param aanalyte: A list of lists of alpha values for the analyte at each h value
    :param atitrant: A list of lists of alpha values for the titrant at each h value

    """

    limiter = len(pka_vals)

    good_val_index = np.where((phi >= 0) & (phi <= limiter+1))

    vol = vol[good_val_index]
    ph = ph[good_val_index]
    h = h[good_val_index]
    oh = oh[good_val_index]

    # Trim the alpha_analyte values
    try:  # If the analyte is strong, there should be no alpha values
        new_alpha_analyte = []
        for key in aanalyte:
            key = int(key)
            aanalyte[key] = aanalyte[key].astype("object")
            new_list = np.insert(aanalyte[key][good_val_index], 0, key)
            new_alpha_analyte.append(new_list)

        new_alpha_analyte = np.array(new_alpha_analyte, dtype="object")
        new_alpha_analyte = np.transpose(new_alpha_analyte)
    except:
        new_alpha_analyte = [[1]]


    # Trim the alpha_titrant values
    try:  # If the titrant is strong, there should be no alpha values
        new_alpha_titrant = []
        for key in atitrant:
            key = int(key)
            atitrant[key] = atitrant[key].astype("object")
            new_list = np.insert(atitrant[key][good_val_index], 0, key)
            new_alpha_titrant.append(new_list)
    except:
        new_alpha_titrant = [[1]]

    new_alpha_titrant = np.array(new_alpha_titrant, dtype="object")
    new_alpha_titrant = np.transpose(new_alpha_titrant)


    return vol, ph, h, oh, phi, new_alpha_analyte, new_alpha_titrant


def equiv_volume(c1, v1, c2):
    """Returns the equivalence volume"""
    c1 = float(c1)
    v1 = float(v1)
    c2 = float(c2)

    return c1 * v1 / c2


def start_phs(min_ph=0, max_ph=14, precision=0.001):
    """Generate pH, [H+], and [OH-] lists"""
    # pH
    ph = np.array(np.arange(min_ph, max_ph + precision, step=precision))
    ph = ph.round(decimals=3)

    # Hydroxide and Hydronium
    h = 10 ** (-ph.copy())
    oh = kw / h
    return ph, h, oh


def check_for_ext(file_name, ext):
    """
    Checks that the input has a certain extension. If it doesn't, it will add the correct extension to the end.

    :param file_name: String to be checked for an extension
    :param ext: Extension (Ex: .txt, .csv, .pdb) to be looked for in the file_name

    Returns the name of the file with the extension.
    """

    has_ext = file_name.find(ext) != -1

    if not has_ext:
        file_name = file_name + ext

    return file_name


def pka_to_ka(pka):
    """Converts a pka, or an array or pka's to a ka or an array of ka's"""
    return np.array(10. ** - np.array(pka))


def scale_alphas(arr):
    """Scale every value in the sublist of the array by its index."""
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


def cond_add_sub(a, b, cond):
    if cond:
        return np.add(a, b)
    else:
        return np.subtract(a, b)


def alpha_values(k, h, base=False, strong=False, kw=(1.023 * (10 ** -14))):
    """
    For a given list of K values, and a list of hydronium concentrations,
    return a list of the alpha values for every level of protonation.

    Parameters:
        k: A list of values for k. --> [k1, k2,..., kn]
        h: A list of hydronium concentrations. --> [h_1, h_2, ..., h_m]
        base: If the solution is a base, the k values need to be converted from Kb to Ka for these calculations.
        strong: If the solution is a strong acid or base, there are no alpha values to be calculated
        kw: Used in the conversion from Kb to Ka. Initially assumes a temperature of 25°C
    """
    if strong:
        return np.array([[1]])

    # Convert lists to numpy arrays for easier math
    h = np.array(h)
    k = np.array(k)

    # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n , K_2 = K_w / K_(n-1)
    if base:
        k = kw / np.flip(k)

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


def get_vol(alpha_analyte, conc_analyte, volume_analyte, alpha_titrant, conc_titrant, h, oh, acid_titrant):
    """
    Take in a whole bunch of information, returns a list of volumes for the given data, with a length equal to the
    [H+] and [OH-] lists.

    :param alpha_analyte: Alpha Analyte
    :param conc_analyte: Concentration Analyte
    :param volume_analyte: Volume Analyte
    :param alpha_titrant: Alpha Titrant
    :param conc_titrant: Concentration Titrant
    :param h: Concentration Hydronium. Must be the same length of oh.
    :param oh: Concentration Hydroxide. Must be the same length of h.
    :param acid_titrant: Whether or not the titrant is an acid.

    :return vol: An array of volumes for the given [H+] and [OH-]
    :return phi: An array of phi (fraction of the way to the equivalence point) values
    """

    # Alpha values scaled by their index
    scaled_alphas_analyte = scale_alphas(alpha_analyte)
    scaled_alphas_titrant = scale_alphas(alpha_titrant)

    # Sume the scaled alpha values. Axis=1 forces the summation to occur for each individual [H+] value.
    summed_scaled_alphas_analyte = np.sum(scaled_alphas_analyte, axis=1)
    summed_scaled_alphas_titrant = np.sum(scaled_alphas_titrant, axis=1)

    beta = h - oh  # No technical definition

    # Conditional addition or subtraction based on the titrant.
    if acid_titrant:
        numerator = summed_scaled_alphas_analyte + (beta / conc_analyte)
        denominator = summed_scaled_alphas_titrant - (beta / conc_titrant)
    else:
        numerator = summed_scaled_alphas_analyte - (beta / conc_analyte)
        denominator = summed_scaled_alphas_titrant + (beta / conc_titrant)

    # Solve for the volume
    phi = numerator / denominator
    volume = phi * volume_analyte * conc_analyte / conc_titrant

    return volume, phi

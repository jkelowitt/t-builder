import numpy as np


def pka_to_ka(pka):
    """Converts a pka, or an array or pka's to a ka or an array of ka's"""
    return 10. ** (-pka)  # Can't raise an int to a non-int datatype.


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
        return a + b
    else:
        return a - b


def alpha_values(k, h, base=False, strong=False, kw=(1.023 * (10 ** -14))):
    """
    For a given list of K values, and a list of hydronium concentrations,
    return a list of the alpha values for every level of protonation.

    Parameters:
        k: An ordered list of values for k. --> [k1, k2,..., kn]
        h: A list of hydronium concentrations. --> [h_1, h_2, ..., h_m]
        base: If the solution is a base, the k values need to be converted from Kb to Ka for these calculations.
        strong: If the solution is a strong acid or base, there are no alpha values to be calculated
        kw: Used in the conversion from Kb to Ka. Initially assumes a temperature of 25°C
    """
    if strong:
        return [[1]]

    # Convert lists to numpy arrays for easier math
    h = np.array(h)
    k = np.array(k)

    # If the k values are for K_b, convert to K_a. --> K_1 = K_w / K_n || K_2 = K_w / K_(n-1)
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

    return alphas

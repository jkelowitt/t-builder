"""
All general use functions in the program. Used Basically everywhere.
"""

import numpy as np

kw = 1.023 * (10 ** -14)  # At 25 degrees celsius


def check_vals(vol, ph, h, oh, alpha, ev):
    """Find only the useful data."""
    # Inbetween 0 added titrant and 2 times equivalence point titrant.

    good_val_index = np.where((vol >= 0) & (vol <= 2 * ev))

    vol = vol[good_val_index]
    ph = ph[good_val_index]
    h = h[good_val_index]
    oh = oh[good_val_index]

    # Trim the alpha values
    new_alpha = []
    for key in alpha:
        alpha[key] = alpha[key].astype("object")
        new_list = np.insert(alpha[key][good_val_index], 0, key)
        new_alpha.append(new_list)

    new_alpha = np.array(new_alpha, dtype="object")

    return vol, ph, h, oh, new_alpha


def equiv_volume(c1, v1, c2):
    """Returns the equivalence volume"""
    c1 = float(c1)
    v1 = float(v1)
    c2 = float(c2)

    return c1 * v1 / c2


def start_phs():
    """Generate pH, [H+], and [OH-] lists"""
    # pH
    ph = np.array(np.arange(0, 14.001, step=0.001))
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

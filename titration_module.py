"""
All general use functions in the program. Used Basically everywhere.
"""

import numpy as np

kw = 1.023 * (10 ** -14)  # At 25 degrees celsius


def check_vals(vol, ph, h, oh, alpha, ev):
    """Find only the useful data."""
    # Inbetween 0 added titrant and 2 times equivalence point titrant.
    good_val_index = np.where([vol <= 2 * ev, vol >= 0])
    vol = [vol[i] for i in good_val_index]
    ph = [ph[i] for i in good_val_index]
    h = [h[i] for i in good_val_index]
    oh = [oh[i] for i in good_val_index]

    # Trim the alpha values
    new_alpha = []
    for obj in alpha:
        cut_alpha = [obj[i] for i in good_val_index]
        new_alpha.append(cut_alpha)

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


def plot_titr(ph, vol, gui, title=""):
    # Clear the plot. This stops matplotlib from plotting over the same plot and hogging up ram.
    ax = gui.plot.ax
    ax.clear()

    # Make the figure, and plot it to the Gui
    ax.plot(vol, ph)
    ax.figure.canvas.draw()


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

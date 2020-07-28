import numpy as np

kw = 1.023 * (10 ** -14)  # At 25 degrees celsius


def check_vals(vol, ph, ev):
    """Get rid of things which are out of range."""
    bad_val_index = np.where([vol >= 2 * ev, vol < 0])
    vol = np.delete(vol, bad_val_index)
    ph = np.delete(ph, bad_val_index)
    return vol, ph


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


def plot_titr(ph, vol, gui, title, xscale=1):
    ax = gui.plot.ax
    ax.clear()
    ax.plot(vol, ph)
    ax.figure.canvas.draw()
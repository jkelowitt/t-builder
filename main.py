"""All of the logic for the functions in the gui"""

import csv

from guietta import ___

from guis import *
from titration_module import *


def get_fig_name(*args):
    # Get the figure's name
    save_fig_gui.run()


def save_plot(*args):
    ax = gui.plot.ax
    fname = check_for_ext(save_fig_gui.figure_name, ".png")

    # Save the figure
    ax.figure.savefig(fname)


def get_csv_name(*args):
    save_csv_gui.run()


def save_csv(*args):
    scg = save_csv_gui

    # Make a list of zipped lists
    fname = check_for_ext(scg.csv_name, ".csv")

    with open(fname, "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)

        # Header row
        csv_writer.writerow(["Name", "Concentration (M)", "Volume (mL)", "K1", "K2", "K3"])

        csv_writer.writerow(scg.ana)
        csv_writer.writerow(scg.titr)

        # Spacer row before data dump
        csv_writer.writerow([])

        # This slows things down, but its used only here, and allows insertion of the row title.
        # Changes the list type from float to object so that strings can be inserted.
        ph = scg.lists[0].astype('object')
        h = scg.lists[1].astype('object')
        oh = scg.lists[2].astype('object')
        vol = scg.lists[4].astype('object')

        # Already an object array
        alpha = scg.lists[3]

        # Add the headers
        ph = np.insert(ph, 0, "pH")
        h = np.insert(h, 0, "[H+]")
        oh = np.insert(oh, 0, "[OH-]")
        vol = np.insert(vol, 0, "Volume Titrant (mL)")

        # Transposes the direction of the values. Now each pH correlates to the same rows h, oh, vol, and the fraction
        zipped = np.dstack((ph, h, oh, vol, *alpha))

        # Write to the csv
        for item in zipped:
            csv_writer.writerows(item)


def run_var_gui(*args):
    base_list = [["<center><u>Titrant Variables", ___],
                 ["Name", "__tname__"],
                 ["Concentration (M):", "__tconc__"],
                 ]

    # Figure out whether its pK'a' or pK'b'
    if gui.aacid.isChecked():
        n = "a"
        t = "b"
    else:
        n = "b"
        t = "a"

    # Add on all of the pK'TITRANT' values, so long as they aren't strong.
    if not gui.tstrong.isChecked():
        for i in range(int(float(gui.tfunc))):
            new_row = [f"pK{t}<sub>{i + 1}</sub>:", f"__pkt{i + 1}__"]
            base_list.append(new_row)

    # Add titrant basics
    t_list = [
        ["<center><u>Analyte Variables", ___],
        ["Name", "__aname__"],
        ["Concentration (M):", "__aconc__"],
        ["Volume (mL):", "__avol__"]
        ]

    for item in t_list:
        base_list.append(item)

    # Add on all of the pK'ANALYTE' values, so long as they aren't strong.
    if not gui.astrong.isChecked():
        for i in range(int(float(gui.afunc))):
            new_row = [f"pK{n}<sub>{i + 1}</sub>:", f"__pka{i + 1}__"]
            base_list.append(new_row)

    base_list.append([(["Plot Titration Curve"], "ptr"), ___])

    var_gui = Gui(*base_list)
    var_gui.ptr = replot
    var_gui.title("Variable Setter")

    var_gui.run()


def replot(var_gui, *args):
    """Plot the titration curve based on the current state of the Guis"""

    """Calculate the Volumes"""
    # Errors with these being used before reference are annoying at worst, so here they are.
    ph, h, oh = start_phs()

    # Collect the pKa/b values and convert them to Ka/b values
    pkt = []
    for i in range(int(float(gui.tfunc))):
        try:
            exec(f"pkt.append(var_gui.pkt{i + 1})")
        except:
            pass

    pka = []
    for i in range(int(float(gui.tfunc))):
        try:
            exec(f"pkt.append(var_gui.pka{i + 1})")
        except:
            pass

    # Convert the pk values to floats.
    pkt = list(map(float, pkt))
    pka = list(map(float, pka))

    kt = pka_to_ka(pkt)
    ka = pka_to_ka(pka)

    conc_analyte = float(var_gui.aconc)
    conc_titrant = float(var_gui.tconc)

    volume_analyte = float(var_gui.avol)
    acid_titrant = gui.tacid.isChecked()

    # Get the alpha values
    alpha_titrant = alpha_values(kt, h)
    alpha_analyte = alpha_values(ka, h)

    # Get the volume and phi values
    vol, phi = get_vol(alpha_analyte, conc_analyte, volume_analyte, alpha_titrant, conc_titrant, h, oh, acid_titrant)

    vol, ph, h, oh, phi, alpha_analyte, alpha_titrant = check_vals(vol, ph, h, oh, phi, gui.afunc, alpha_analyte,
                                                                   alpha_titrant)

    """Plot the graph"""
    # Clear the plot. This stops matplotlib from plotting over the same plot and hogging up ram.
    ax = gui.plot.ax
    ax.clear()

    # Make the figure, and plot it to the Gui
    ax.plot(vol, ph)
    ax.figure.canvas.draw()


# Defining buttons
gui.ForcePlot = replot
gui.start = run_var_gui
gui.SavePlot = get_fig_name
save_fig_gui.SavePlot = save_plot

# CSV saving buttons
gui.SaveCSV = get_csv_name
save_csv_gui.SaveCSV = save_csv

if __name__ == "__main__":
    gui.run()

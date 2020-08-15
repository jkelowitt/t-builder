"""All of the logic for the functions in the gui"""

import csv
from guietta import Gui, ___, Exceptions, Ok, Quit, III, VSeparator, HSeparator, R, R1, R2, M, _

from guis import *
from titration_module import *


# Main Gui. Shows on startup.


# @gui.auto
def replot(gui, *args):
    """Plot the titration curve based on the current state of the Guis"""

    # Errors with these being used before reference are annoying at worst, so here they are.
    vol, ph, ev = [], [], 0

    """Button states. Used to determine which titration equations are used."""
    # Functionality of the analyte
    mono = gui.Monoprotic.isChecked()

    """Plot the graph"""
    # Clear the plot. This stops matplotlib from plotting over the same plot and hogging up ram.
    ax = gui.plot.ax
    ax.clear()

    # Make the figure, and plot it to the Gui
    ax.plot(vol, ph)  # np arrays have the type at index 1, therefore the specificity
    ax.figure.canvas.draw()


def get_fig_name(gui, *args):
    # Get the figure's name
    save_fig_gui.run()


def save_plot(gui, *args):
    ax = gui.plot.ax
    fname = check_for_ext(save_fig_gui.figure_name, ".png")

    # Save the figure
    ax.figure.savefig(fname)


def get_csv_name(gui, *args):
    save_csv_gui.run()


def save_csv(gui, *args):
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


# Replot button function definition
gui.ForcePlot = replot

# Plot saving buttons
gui.SavePlot = get_fig_name
save_fig_gui.SavePlot = save_plot

# CSV saving buttons
gui.SaveCSV = get_csv_name
save_csv_gui.SaveCSV = save_csv

# Name the main window
gui.title("Titration Plotter")

if __name__ == "__main__":
    gui.run()

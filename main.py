"""All of the logic for the functions in the gui"""

from guietta import M, ___, III, R1, R2, VSeparator, HSeparator, Quit, _
import csv

from monoprotic_module import *
from diprotic_module import *
from triprotic_module import *
from sub_guis import *

# Main Gui. Shows on startup.
gui = Gui(
    [M("plot"), VSeparator, "Titrant"            , VSeparator , "Analyte"       ],
    [III      , III       , R1("Strong Acid")    , III        , R2("Monoprotic")],
    [III      , III       , R1("Strong Base")    , III        , R2("Diprotic")  ],
    [III      , III       , _                    , III        , R2("Triprotic") ],
    [III      , III       , HSeparator           , ___        , ___             ],
    [III      , III       , ["Assign Parameters"], _          , ["Force Plot"]  ],
    [III      , III       , ["Save CSV"]         , _          , ["Save Plot"]   ],
    [III      , III       , HSeparator           , ___        , ___             ],
    [III      , III       , Quit                 , ___        , ___             ],
    exceptions=Exceptions.PRINT
    )

# @gui.auto
def replot(gui, *args):
    """Plot the titration curve based on the current state of the Guis"""

    # Errors with these being used before reference are annoying at worst, so here they are.
    vol, ph, ev = [], [], 0

    """Button states. Used to determine which titration equations are used."""
    # Functionality of the analyte
    mono = gui.Monoprotic.isChecked()
    di = gui.Diprotic.isChecked()
    tri = gui.Triprotic.isChecked()

    # Whether the acid or the base is the titrant
    acid = gui.StrongAcid.isChecked()
    base = gui.StrongBase.isChecked()

    # Special states for just the monoprotic acids
    sba = mp_sa.Strong.isChecked()  # Strong base analyte
    wba = mp_sa.Weak.isChecked()  # Weak base analyte

    saa = mp_sb.Strong.isChecked()  # Strong acid analyte
    waa = mp_sb.Weak.isChecked()  # Weak acid analyte


    """Titration calculations. LMK if there is a better way to do these conditionals."""
    # Monoprotic, Using a strong acid titrant
    if mono and acid:
        m = mp_sa
        if sba:  # To titrate a strong base analyte
            # Start the data creation
            m = mp_sa
            ev = equiv_volume(m.mpbc, m.mpbv, m.mpac)
            vol, ph, h, oh, alpha = mp_sbsa(m.mpbc, m.mpbv, m.mpac)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (m.mpbn, m.mpbc, m.mpbv)
            save_csv_gui.titr = (m.mpan, m.mpac)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

        elif wba:  # To titrate a weak base analyte
            # Start the data creation
            ev = equiv_volume(m.mpbc, m.mpbv, m.mpac)
            vol, ph, h, oh, alpha = mp_wbsa(m.mpbk, m.mpbc, m.mpac, m.mpbv)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (m.mpbn, m.mpbc, m.mpbv, m.mpbk)
            save_csv_gui.titr = (m.mpan, m.mpac)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

    # Monoprotic, Using a strong base titrant
    elif mono and base:
        m = mp_sb
        if saa:  # Strong acid analyte
            # Start the data creation
            ev = equiv_volume(m.mpac, m.mpav, m.mpbc)
            vol, ph, h, oh, alpha = mp_sasb(m.mpac, m.mpav, m.mpbc)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (m.mpan, m.mpac, m.mpav)
            save_csv_gui.titr = (m.mpbn, m.mpbc)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

        elif waa:  # Weak acid analyte
            # Start the data creation
            ev = equiv_volume(m.mpac, m.mpav, m.mpbc)
            vol, ph, h, oh, alpha = mp_wasb(m.mpak, m.mpac, m.mpbc, m.mpav)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (m.mpan, m.mpac, m.mpav, m.mpak)
            save_csv_gui.titr = (m.mpbn, m.mpbc)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

    # Diprotic
    elif di:

        if acid:  # Acid Titrant, Weak Diprotic Base Analyte
            # Start the data creation
            d = dp_sa
            ev = equiv_volume(d.dpbc, d.dpbv, d.dpac) * 2  # I need a better way to adjust the scaling
            vol, ph, h, oh, alpha = dp_wbsa(d.dpbk1, d.dpbk2, d.dpac, d.dpbc, d.dpbv)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (d.dpbn, d.dpbc, d.dpbv, d.dpbk1, d.dpbk2)
            save_csv_gui.titr = (d.dpan, d.dpac)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

        elif base:  # Base Titrant, Weak Diprotic Acid Analyte
            # Start the data creation
            d = dp_sb
            ev = equiv_volume(d.dpac, d.dpav, d.dpbc) * 2
            vol, ph, h, oh, alpha = dp_wasb(d.dpak1, d.dpak2, d.dpac, d.dpbc, d.dpav)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (d.dpan, d.dpac, d.dpav, d.dpak1, d.dpak2)
            save_csv_gui.titr = (d.dpbn, d.dpbc)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

    # Triprotic
    elif tri:

        if acid:  # Acid Titrant
            # Start the data creation
            t = tp_sa
            ev = equiv_volume(t.tpbc, t.tpbv, t.tpac) * 3
            vol, ph, h, oh, alpha = tp_wbsa(t.tpbk1, t.tpbk2, t.tpbk3, t.tpac, t.tpbc, t.tpbv)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (t.tpbn, t.tpbc, t.tpbv, t.tpbk1, t.tpbk2)
            save_csv_gui.titr = (t.tpan, t.tpac)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

        elif base:  # Base Titrant
            # Start the data creation
            t = tp_sb
            ev = equiv_volume(t.tpac, t.tpav, t.tpbc) * 3
            vol, ph, h, oh, alpha = tp_wasb(t.tpak1, t.tpak2, t.tpak3, t.tpac, t.tpbc, t.tpav)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            save_csv_gui.ana = (t.tpan, t.tpac, t.tpav, t.tpak1, t.tpak2, t.tpak3)
            save_csv_gui.titr = (t.tpbn, t.tpbc)
            save_csv_gui.lists = (ph, h, oh, alpha, vol)

    """Plot the graph"""
    # Clear the plot. This stops matplotlib from plotting over the same plot and hogging up ram.
    ax = gui.plot.ax
    ax.clear()

    # Make the figure, and plot it to the Gui
    ax.plot(vol, ph)  # np arrays have the type at index 1, therefore the specificity
    ax.figure.canvas.draw()


def open_nui(gui):
    """Opens the sub gui's based on button states"""

    # Analyte functionality
    mono = gui.Monoprotic.isChecked()
    di = gui.Diprotic.isChecked()
    tri = gui.Triprotic.isChecked()

    # Titrant identity
    acid = gui.StrongAcid.isChecked()
    base = gui.StrongBase.isChecked()

    # Monoprotic guis
    if mono and acid:
        mp_sa.run()
    elif mono and base:
        mp_sb.run()

    # Diprotic guis
    elif di and acid:
        dp_sa.run()
    elif di and base:
        dp_sb.run()

    # Triprotic guis
    elif tri and acid:
        tp_sa.run()
    elif tri and base:
        tp_sb.run()


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

# Open the sub guis on command
gui.AssignParameters = open_nui

if __name__ == "__main__":
    gui.run()

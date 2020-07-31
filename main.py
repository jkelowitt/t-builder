"""All of the logic for the functions in the gui"""

from guietta import M, ___, III, R1, R2, VSeparator, HSeparator, Quit, _
import types
import csv

from monoprotic_module import *
from diprotic_module import *
from triprotic_module import *
from sub_guis import *

# An object to grab all the data from each of the titrations.
data = types.SimpleNamespace()


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
    [_        , _         , Quit                 , ___        , ___             ],
    exceptions=Exceptions.PRINT
    )

@gui.auto
def replot(gui, data, *args):
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

    # Clear the data object
    data.ana = ()
    data.titr = ()
    data.lists = ()

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
            data.ana = (m.mpbn, m.mpbc, m.mpbv)
            data.titr = (m.mpan, m.mpac)
            data.lists = (ph, h, oh, alpha, vol)

        elif wba:  # To titrate a weak base analyte
            # Start the data creation
            ev = equiv_volume(m.mpbc, m.mpbv, m.mpac)
            vol, ph, h, oh, alpha = mp_wbsa(m.mpbk, m.mpbc, m.mpac, m.mpbv)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            data.ana = (m.mpbn, m.mpbc, m.mpbv, m.mpbk)
            data.titr = (m.mpan, m.mpac)
            data.lists = (ph, h, oh, alpha, vol)

    # Monoprotic, Using a strong base titrant
    elif mono and base:
        m = mp_sb
        if saa:  # Strong acid analyte
            # Start the data creation
            ev = equiv_volume(m.mpac, m.mpav, m.mpbc)
            vol, ph, h, oh, alpha = mp_sasb(m.mpac, m.mpav, m.mpbc)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            data.ana = (m.mpan, m.mpac, m.mpav)
            data.titr = (m.mpbn, m.mpbc)
            data.lists = (ph, h, oh, alpha, vol)

        elif waa:  # Weak acid analyte
            # Start the data creation
            ev = equiv_volume(m.mpac, m.mpav, m.mpbc)
            vol, ph, h, oh, alpha = mp_wasb(m.mpak, m.mpac, m.mpbc, m.mpav)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            data.ana = (m.mpan, m.mpac, m.mpav, m.mpak)
            data.titr = (m.mpbn, m.mpbc)
            data.lists = (ph, h, oh, alpha, vol)

    # Diprotic
    elif di:

        if acid:  # Acid Titrant, Weak Diprotic Base Analyte
            # Start the data creation
            d = dp_sa
            ev = equiv_volume(d.dpbc, d.dpbv, d.dpac) * 2  # I need a better way to adjust the scaling
            vol, ph, h, oh, alpha = dp_wbsa(d.dpbk1, d.dpbk2, d.dpac, d.dpbc, d.dpbv)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            data.ana = (d.dpbn, d.dpbc, d.dpbv, d.dpbk1, d.dpbk2)
            data.titr = (d.dpan, d.dpac)
            data.lists = (ph, h, oh, alpha, vol)

        elif base:  # Base Titrant, Weak Diprotic Acid Analyte
            # Start the data creation
            d = dp_sb
            ev = equiv_volume(d.dpac, d.dpav, d.dpbc) * 2
            vol, ph, h, oh, alpha = dp_wasb(d.dpak1, d.dpak2, d.dpac, d.dpbc, d.dpav)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            data.ana = (d.dpan, d.dpac, d.dpav, d.dpak1, d.dpak2)
            data.titr = (d.dpbn, d.dpbc)
            data.lists = (ph, h, oh, alpha, vol)

    # Triprotic
    elif tri:

        if acid:  # Acid Titrant
            # Start the data creation
            t = tp_sa
            ev = equiv_volume(t.tpbc, t.tpbv, t.tpac) * 3
            vol, ph, h, oh, alpha = tp_wbsa(t.tpbk1, t.tpbk2, t.tpbk3, t.tpac, t.tpbc, t.tpbv)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            data.ana = (t.tpbn, t.tpbc, t.tpbv, t.tpbk1, t.tpbk2)
            data.titr = (t.tpan, t.tpac)
            data.lists = (ph, h, oh, alpha, vol)

        elif base:  # Base Titrant
            # Start the data creation
            t = tp_sb
            ev = equiv_volume(t.tpac, t.tpav, t.tpbc) * 3
            vol, ph, h, oh, alpha = tp_wasb(t.tpak1, t.tpak2, t.tpak3, t.tpac, t.tpbc, t.tpav)
            vol, ph, h, oh, alpha = check_vals(vol, ph, h, oh, alpha, ev)

            # Collect the data
            data.ana = (t.tpan, t.tpac, t.tpav, t.tpak1, t.tpak2, t.tpak3)
            data.titr = (t.tpbn, t.tpbc)
            data.lists = (ph, h, oh, alpha, vol)

    """Plot the graph"""
    plot_titr(ph, vol, gui)


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


def get_fig_name(gui):
    # Get the figure's name
    save_fig_gui.run()


def save_plot(gui):
    ax = gui.plot.ax
    fname = check_for_ext(save_fig_gui.figure_name, ".png")

    # Save the figure
    ax.figure.savefig(fname)


def get_csv_name(gui):
    save_csv_gui.run()


def save_csv(gui, data):
    zipped = zip(data.lists[0], data.lists[1], data.lists[2], data.lists[3], data.lists[4])
    with open(save_csv_gui.csv_name, "w") as new_file:
        csv_reader = csv.writer(new_file)

        csv_reader.writerow(data.ana)
        csv_reader.writerow(data.titr)
        csv_reader.writerow("")
        for item in zipped:
            csv_reader.writerow(item)


"""
 data.ana = (t.tpan, t.tpac, t.tpav, t.tpak1, t.tpak2, t.tpak3)
 data.titr = (t.tpbn, t.tpbc)
 data.lists = (ph, h, oh, alpha, vol)
"""


# When the button is pressed, do the thing
gui.ForcePlot = replot
gui.AssignParameters = open_nui

gui.SavePlot = get_fig_name
save_fig_gui.SavePlot = save_plot

gui.SaveCSV = get_csv_name
save_csv_gui.SaveCSV = save_csv

# Name the window
gui.title("Titration Plotter")

# Open the sub guis on command
gui.AssignParameters = open_nui

gui.run()

"""All of the logic for the functions in the gui"""

from guietta import M, ___, III, R1, R2, VSeparator, HSeparator, Quit, _

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
    [_        , _         , Quit                 , ___        , ___             ],
    exceptions=Exceptions.PRINT
    )


@gui.auto
def replot(gui, *args):
    """Plot the titration curve based on the current state of the Guis"""

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

        if sba:  # To titrate a strong base analyte
            ev = equiv_volume(mp_sa.mpbc, mp_sa.mpbv, mp_sa.mpac)
            vol, ph = sbsa(mp_sa.mpbc, mp_sa.mpbv, mp_sa.mpac)

        elif wba:  # To titrate a weak base analyte
            ev = equiv_volume(mp_sa.mpbc, mp_sa.mpbv, mp_sa.mpac)
            vol, ph = wbsa(mp_sa.mpbk, mp_sa.mpbc, mp_sa.mpac, mp_sa.mpbv)

    # Monoprotic, Using a strong base titrant
    elif mono and base:

        if saa:  # Strong acid analyte
            ev = equiv_volume(mp_sb.mpac, mp_sb.mpav, mp_sb.mpbc)
            vol, ph = sasb(mp_sb.mpac, mp_sb.mpav, mp_sb.mpbc)

        elif waa:  # Weak acid analyte
            ev = equiv_volume(mp_sb.mpac, mp_sb.mpav, mp_sb.mpbc)
            vol, ph = wasb(mp_sb.mpak, mp_sb.mpac, mp_sb.mpbc, mp_sb.mpav)

    # Diprotic
    elif di:

        if acid:  # Acid Titrant
            ev = equiv_volume(dp_sa.dpbc, dp_sa.dpbv, dp_sa.dpac) * 2
            vol, ph = dp_wbsa(dp_sa.dpbk1, dp_sa.dpbk2, dp_sa.dpac, dp_sa.dpbc, dp_sa.dpbv, base=True)

        elif base:  # Base Titrant
            ev = equiv_volume(dp_sb.dpac, dp_sb.dpav, dp_sb.dpbc) * 2
            vol, ph = dp_wasb(dp_sb.dpak1, dp_sb.dpak2, dp_sb.dpac, dp_sb.dpbc, dp_sb.dpav)

    # Triprotic
    elif tri:

        if acid:  # Acid Titrant
            ev = equiv_volume(tp_sa.tpbc, tp_sa.tpbv, tp_sa.tpac) * 3
            vol, ph = tp_wbsa(tp_sa.tpbk1, tp_sa.tpbk2, tp_sa.tpbk3, tp_sa.tpac, tp_sa.tpbc, tp_sa.tpbv)
        elif base:  # Base Titrant
            ev = equiv_volume(tp_sb.tpac, tp_sb.tpav, tp_sb.tpbc) * 3
            vol, ph = tp_wasb(tp_sb.tpak1, tp_sb.tpak2, tp_sb.tpak3, tp_sb.tpac, tp_sb.tpbc, tp_sb.tpav)

    # Remove all extraneous values (Volumes less than zero, or obscenely large)
    vol, ph = check_vals(vol, ph, ev)

    """Plot the graph"""

    # Clear the plot. This stops matplotlib from plotting over the same plot and hogging up ram.
    ax = gui.plot.ax
    ax.clear()

    # Make the figure, and plot it to the Gui
    ax.plot(vol, ph)
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


def save_csv(gui):
    # Vastly more complicated than what I have the patience for right now.
    # Probably involves saving all of the data input above, running the results, and
    # then formatting the data correctly. Much more painstaking than originally expected.
    print("Test Statement")
    pass


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

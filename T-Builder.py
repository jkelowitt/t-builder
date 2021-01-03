from dearpygui.core import *
from dearpygui.simple import *
from webbrowser import open

from titration_class import Compound, Titration

__author__ = "jkelowitt"
__version__ = "v2.3.4"
__license__ = "MIT"

plot_width = 905
plot_height = 755
data_width = 200


def open_link(sender, data):
    open("https://github.com/jkelowitt/t-builder", new=2)


def query(sender, data):
    set_plot_xlimits(sender, data[0], data[1])
    set_plot_ylimits(sender, data[2], data[3])


def make_titration():
    # Create compounds
    Analyte = Compound(
        name=get_value("Analyte Name"),
        acidic=get_value("aa"),
        pKs=[float(i) for i in get_value("apk").split(",")],
        strong=get_value("as"),
    )

    Titrant = Compound(
        name=get_value("tname"),
        acidic=not get_value("aa"),
        pKs=[float(i) for i in get_value("tpk").split(",")],
        strong=get_value("ts"),
    )

    # Create titration object
    titr = Titration(
        analyte=Analyte,
        titrant=Titrant,
        concentration_analyte=get_value("aconc"),
        concentration_titrant=get_value("tconc"),
        volume_analyte=get_value("avol"),
        precision=get_value("precision"),
        temp=get_value("temperature"),
    )

    return titr


def plot_callback(sender, data):
    clear_plot("Main Plot")

    # Band-aid fix to issue #10. Everything which needs to be kept in a certain range must have callback_data
    try:
        value = get_value(sender)
        if value < data[0]:
            set_value(sender, data[0])
            clear_plot("Main Plot")
            return
    except:  # If the widget doesn't give you a number to check, don't check its value.
        pass

    titr = make_titration()

    # These are the only variables which could change the bjerrum plot
    who_sent = get_all_items().copy()

    if sender == "b_tab_button":  # Everything but the buffer tab button
        # Perform bjerrum calculations
        bx = list(titr.ph)
        bys = [list(alpha) for alpha in titr.alpha_analyte.T]

        # For every alpha value list, plot the alpha values at every pH and add the line to the plot
        for num, alpha in enumerate(bys):
            add_line_series(plot="Main Plot", name=f"species{num}", x=bx, y=alpha, weight=2)

    else:
        # Perform titration calculations
        tx = list(titr.volume_titrant_t)
        ty = list(titr.ph_t)

        # plot the calculations
        add_line_series(
            plot="Main Plot",
            name="Titration Curve",
            x=tx,
            y=ty,
            weight=2,
            color=[0, 255, 255, 255],
        )

        if get_value("buffer_regions"):
            vols, pHs = titr.find_buffer_points()

            vols = list(vols)
            pHs = list(pHs)

            add_scatter_series(
                plot="Main Plot",
                name="Buffer Points",
                x=vols,
                y=pHs,
                fill=[255, 0, 0, 255],
                outline=[255, 0, 0, 255],
                weight=2,
            )

            # Add labels to the volumes of each point
            for vol, pH in zip(vols, pHs):
                if titr.analyte_is_acidic:
                    add_annotation("Main Plot", x=vol, y=pH, text=f"{vol:.5g} mL", xoffset=5, yoffset=5)
                else:
                    # Annotations need to be above the line if the solution is basic to prevent the line from clipping
                    add_annotation(
                        "Main Plot",
                        x=vol,
                        y=pH,
                        text=f"{vol:.5g} mL",
                        xoffset=5,
                        yoffset=-5,
                    )

        if get_value("equiv"):
            vols, pHs = titr.find_equiv_points()

            vols = list(vols)
            pHs = list(pHs)

            add_scatter_series(
                plot="Main Plot",
                name="Equivalence Points",
                x=vols,
                y=pHs,
                fill=[0, 255, 0, 255],
                outline=[0, 255, 0, 255],
                weight=2,
            )

            # Add labels to the volumes of each point
            for vol, pH in zip(vols, pHs):
                if titr.analyte_is_acidic:
                    add_annotation("Main Plot", x=vol, y=pH, text=f"{vol:.5g} mL", xoffset=5, yoffset=5)
                else:
                    # Annotations need to be above the line if the solution is basic to prevent the line from clipping
                    add_annotation(
                        "Main Plot",
                        x=vol,
                        y=pH,
                        text=f"{vol:.5g} mL",
                        xoffset=5,
                        yoffset=-5,
                    )

        if get_value("1stderiv"):
            volume, pHderiv = titr.deriv(degree=1)

            data = titr.scale_data(pHderiv, get_value("1dscaler"))

            add_line_series(
                plot="Main Plot",
                name="First Derivative",
                x=list(volume),
                y=list(data),
                weight=2,
                color=[255, 0, 255, 255],
            )

        if get_value("2ndderiv"):
            volume, pHderiv = titr.deriv(degree=2)

            data = titr.scale_data(pHderiv, get_value("2dscaler"))

            add_line_series(
                plot="Main Plot",
                name="Second Derivative",
                x=list(volume),
                y=list(data),
                weight=2,
                color=[255, 255, 0, 255],
            )


def save_titr_data(sender, data):
    titr = make_titration()
    title = f"{get_value('aname')}_{get_value('tname')}_titration".replace(" ", "_")
    titr.write_titration_data(title=title)


def save_bjer_data(sender, data):
    titr = make_titration()
    title = f"{get_value('aname')}_{get_value('tname')}_species".replace(" ", "_")
    titr.write_alpha_data(title=title)


def save_ana_data(sender, data):
    titr = make_titration()
    title = f"{get_value('aname')}_{get_value('tname')}_analysis".replace(" ", "_")
    titr.write_analysis_data(title=title)


# Main gui formatting
with window("Main Window", label="Something Else", autosize=True):
    set_main_window_size(width=1270, height=850)

    # Project name

    with tab_bar("Main Tab bar"):
        add_tab_button("t_tab_button", label="Titration", callback=plot_callback)
        add_tab_button("b_tab_button", label="Speciation", callback=plot_callback)

        add_same_line()
        add_text(" " * 129)  # TODO ask for right adjust text on DPG
        add_same_line()
        add_button("T-Builder by Jkelowitt", callback=open_link, tip="Open in github in browser")

        with group("Data Entry", width=data_width):
            add_text("Analyte Data")
            add_input_text(
                "aname",
                label="Name",
                default_value="Citric Acid",
                callback=plot_callback,
                tip="Enter the name of the analyte. This is used when making the data files.",
            )

            add_input_float(
                "aconc",
                label="Concentration (M)",
                default_value=0.10,
                callback=plot_callback,
                callback_data=[0],
                tip="Enter the concentration of the analyte in molarity.",
            )

            add_input_text(
                "apk",
                label="pK value(s)",
                default_value="3.13, 4.76, 6.40",
                callback=plot_callback,
                tip="Enter the pK values of the analyte. Separate them with commas if there are more than one.",
            )

            add_input_float(
                "avol",
                label="Volume (mL)",
                default_value=25,
                callback=plot_callback,
                callback_data=[0],
                tip="Enter the volume of the analyte in mL.",
            )

            add_checkbox(
                "aa",
                label="Acidic",
                default_value=True,
                callback=plot_callback,
                tip="Check this box if the analyte acts as an acid during this titration.",
            )

            add_checkbox(
                "as",
                label="Strong",
                default_value=False,
                callback=plot_callback,
                tip="Check this box if the titrant is a strong acid or base.",
            )

            add_dummy(height=25)
            add_text("Titrant Data")

            add_input_text(
                "tname",
                label="Name",
                default_value="KOH",
                callback=plot_callback,
                tip="Enter the name of the titrant. This is used when naming the data files.",
            )

            add_input_float(
                "tconc",
                label="Concentration (M)",
                default_value=0.10,
                callback=plot_callback,
                callback_data=[0],
                tip="Enter the concentration of the titrant in molarity.",
            )

            add_input_text(
                "tpk",
                label="pK value(s)",
                default_value="0.20",
                callback=plot_callback,
                tip="Enter the pK values of the titrant. Separate them with commas if there are more than one.",
            )

            add_checkbox(
                "ts",
                label="Strong",
                default_value=True,
                callback=plot_callback,
                tip="Check this box if the titrant is a strong acid or base.",
            )

            add_dummy(height=25)
            add_text("Titration Settings")

            add_input_int(
                "precision",
                label="Precision",
                default_value=2,
                callback=plot_callback,
                tip="The number of decimal points to calculate the pH to. (>=1)",
                width=65,
            )

            add_input_int(
                "temperature",
                label="Temperature (C)",
                default_value=25,
                callback=plot_callback,
                tip="The temperature at which the titration occurs. (Most accurate between 0 and 350 C)",
                width=65,
            )

            add_dummy(height=25)
            add_text("Perform Titration Analysis")

            add_checkbox(
                "buffer_regions",
                label="Show Buffering Points",
                default_value=False,
                callback=plot_callback,
                tip="Show the center of the buffering regions on the Titration plot.",
            )

            add_checkbox(
                "equiv",
                label="Show Equivalence Points",
                default_value=False,
                callback=plot_callback,
                tip="Show the equivalence points on the Titration plot.",
            )

            add_checkbox(
                "1stderiv",
                label="Show normalized y'",
                default_value=False,
                callback=plot_callback,
                tip="Show the normalized 1st Derivative of the Titration plot",
            )

            add_checkbox(
                "2ndderiv",
                label="Show normalized y''",
                default_value=False,
                callback=plot_callback,
                tip="Show the normalized 2nd Derivative of the Titration plot.",
            )

            add_drag_float(
                "1dscaler",
                label="Scale y'",
                default_value=8,
                min_value=1,
                speed=0.1,
                width=80,
                format="%0.2f",
                callback=plot_callback,
                tip="Scale the 1st Derivative of the Titration plot.",
            )

            add_drag_float(
                "2dscaler",
                label="Scale y''",
                default_value=2,
                min_value=1,
                speed=0.1,
                width=80,
                format="%0.2f",
                callback=plot_callback,
                tip="Scale the 2nd Derivative of the Titration plot.",
            )

            add_dummy(height=25)
            add_text("Save Data to CSV")
            add_button("Save Titration Data ", callback=save_titr_data)
            add_button("Save Speciation Data", callback=save_bjer_data)
            add_button("Save Analysis Data", callback=save_ana_data)

        # Put the titration curve under the data entry section
        add_same_line()
        with group("TitrationPlotGroup"):
            add_plot(
                "Main Plot",
                label="",
                query_callback=query,
                width=plot_width,
                height=plot_height,
                anti_aliased=True,
            )

    plot_callback("equiv", [])  # Make the plots appear on program start

# Run the curve.
if __name__ == "__main__":
    start_dearpygui(primary_window="Main Window")

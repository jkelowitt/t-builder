from dearpygui.core import *
from dearpygui.simple import *

from titration_class import Compound, Titration

plot_width = 615
plot_height = 510
data_width = 200


def query_titr(sender, data):
    show_item("Plot Window")
    set_plot_xlimits("titration_curve", data[0], data[1])
    set_plot_ylimits("titration_curve", data[2], data[3])


def query_bjer(sender, data):
    show_item("Plot Window")
    set_plot_xlimits("bjerrum_curve", data[0], data[1])
    set_plot_ylimits("bjerrum_curve", data[2], data[3])


def make_titration(sender, data):
    # Create compounds
    Analyte = Compound(name=get_value("Analyte Name"),
                       acidic=get_value("aa"),
                       pKs=[float(i) for i in get_value("apk").split(",")],
                       strong=get_value("as")
                       )

    Titrant = Compound(name=get_value("tname"),
                       acidic=not get_value("aa"),
                       pKs=[float(i) for i in get_value("tpk").split(",")],
                       strong=get_value("ts")
                       )

    # Create titration object
    titr = Titration(analyte=Analyte,
                     titrant=Titrant,
                     concentration_analyte=get_value("aconc"),
                     concentration_titrant=get_value("tconc"),
                     volume_analyte=get_value("avol")
                     )

    return titr


def plot_callback(sender, data):
    clear_plot("Titration")
    clear_plot("Relative Species")

    titr = make_titration(sender, data)

    # Perform titration calculations
    tx = list(titr.volume_titrant_t)
    ty = list(titr.ph_t)

    # plot the calculations
    add_line_series(plot="Titration",
                    name="",
                    x=tx,
                    y=ty,
                    weight=2)

    # Perform bjerrum calculations
    bx = list(titr.ph)
    bys = [list(alpha) for alpha in titr.alpha_analyte.T]

    # For every alpha value list, plot the alpha values at every pH and add the line to the plot
    for num, alpha in enumerate(bys):
        add_line_series(plot="Relative Species",
                        name=f"species{num}",
                        x=bx,
                        y=alpha,
                        weight=2)


def save_titr_data(sender, data):
    titr = make_titration(sender, data)
    title = f"{get_value('aname')}_{get_value('tname')}_titr".replace(' ', '_')
    titr.write_titration_data(title=title)
    with window("File Saved!##1"):
        add_text(f"File saved to {title}.csv")


def save_bjer_data(sender, data):
    titr = make_titration(sender, data)
    title = f"{get_value('aname')}_{get_value('tname')}_bjer".replace(' ', '_')
    titr.write_alpha_data(title=title)
    with window("File Saved!##2"):
        add_text(f"File saved to {title}.csv")


# Main gui formatting
with window("Main Window", label="Something Else"):
    set_main_window_size(width=1270, height=820)

    # Project name
    add_text("T-Builder")
    add_dummy(height=10)

    # Get the analyte data
    with group("Analyte", width=data_width):
        add_text("Analyte Data")
        add_input_text('aname',
                       label="Analyte Name",
                       default_value="Citric Acid",
                       callback=plot_callback,
                       tip="This is used when making the data file."
                       )

        add_input_float('aconc',
                        label="Analyte Concentration (M)",
                        default_value=0.10,
                        callback=plot_callback,
                        tip="Enter the concentration of the analyte in molarity."
                        )

        add_input_text('apk',
                       label="Analyte pK value(s)",
                       default_value="3.13, 4.76, 6.40",
                       callback=plot_callback,
                       tip="Enter the pK values of the analyte. Separate them with commas if there are more than one."
                       )

        add_input_float('avol',
                        label="Analyte Volume (mL)",
                        default_value=25,
                        callback=plot_callback,
                        tip="Enter the volume of the analyte in mL."
                        )

        add_checkbox('aa',
                     label="Analyte is acidic",
                     default_value=True,
                     callback=plot_callback,
                     tip="Check this box if the analyte acts as an acid during this titration."
                     )

        add_checkbox('as',
                     label="Analyte is strong",
                     default_value=False,
                     callback=plot_callback,
                     tip="Check this box if the titrant is a strong acid or base."
                     )

    # Add some spacing between the analyte and titrant data collection
    add_same_line()
    add_dummy(width=10)

    # Get the titrant data
    add_same_line()
    with group("Titrant", width=data_width):
        add_text("Titrant Data")

        add_input_text("tname",
                       label="Titrant Name",
                       default_value="KOH",
                       callback=plot_callback,
                       tip="This is used when naming the data file."
                       )

        add_input_float("tconc",
                        label="Titrant Concentration (M)",
                        default_value=0.10,
                        callback=plot_callback,
                        tip="Enter the concentration of the titrant in molarity."
                        )

        add_input_text("tpk",
                       label="Titrant pK value(s)",
                       default_value="0.20",
                       callback=plot_callback,
                       tip="Enter the pK values of the titrant. Separate them with commas if there are more than one."
                       )

        add_checkbox("ts",
                     label="Titrant is strong",
                     default_value=True,
                     callback=plot_callback,
                     tip="Check this box if the titrant is a strong acid or base."
                     )

    add_button("Plot data", callback=plot_callback, width=data_width * 2)
    add_dummy(height=10)

    # Put the titration curve under the data entry section
    add_next_column()
    with group("TitrationPlotGroup"):
        add_plot("Titration", query_callback=query_titr, width=plot_width, height=plot_height)

        # Put the bjerrum plot to the right of the titration curve
    add_same_line()
    with group("BjerrumPlotGroup"):
        add_plot("Relative Species", query_callback=query_bjer, width=plot_width, height=plot_height)

    with group("SaveData"):
        add_button("Save Titration Data to CSV", callback=save_titr_data)

        add_same_line()
        add_dummy(width=417)

        add_same_line()
        add_button("Save Bjerrum Data to CSV", callback=save_bjer_data)

    # Run the curve.
    start_dearpygui(primary_window="Main Window")

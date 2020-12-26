from dearpygui.core import *
from dearpygui.simple import *
import titration_class as ts

plot_width = 620
data_width = 200


def apply_theme(sender, data):
    theme = get_value("Themes")
    set_theme(theme)


themes = ["Grey", "Dark Grey", "Light", "Dark", "Dark 2", "Classic", "Cherry", "Purple", "Gold", "Red"]


def apply_text_multiplier(sender, data):
    font_multiplier = get_value("Font Size Multiplier")
    set_global_font_scale(font_multiplier)


def query_titr(sender, data):
    show_item("Plot Window")
    set_plot_xlimits("titration_curve", data[0], data[1])
    set_plot_ylimits("titration_curve", data[2], data[3])


def query_bjer(sender, data):
    show_item("Plot Window")
    set_plot_xlimits("bjerrum_curve", data[0], data[1])
    set_plot_ylimits("bjerrum_curve", data[2], data[3])


def plot_callback(sender, data):
    clear_plot("titration_plot")
    clear_plot("bjerrum_plot")

    # Create compounds
    Analyte = ts.Compound(name=get_value("Analyte Name"),
                          acidic=get_value("Analyte is acidic"),
                          pKs=[float(i) for i in get_value("Analyte pK value(s)").split(",")],
                          strong=get_value("Analyte is strong")
                          )

    Titrant = ts.Compound(name=get_value("Titrant Name"),
                          acidic=not get_value("Analyte is acidic"),
                          pKs=[float(i) for i in get_value("Titrant pK value(s)").split(",")],
                          strong=get_value("Titrant is strong")
                          )

    # Create titration object
    titr = ts.Titration(analyte=Analyte,
                        titrant=Titrant,
                        concentration_analyte=get_value("Analyte Concentration (M)"),
                        concentration_titrant=get_value("Titrant Concentration (M)"),
                        volume_analyte=get_value("Analyte Volume (mL)"))

    # Perform titration calculations
    tx = list(titr.volume_titrant_t)
    ty = list(titr.ph_t)

    # plot the calculations
    add_line_series(plot="titration_plot",
                    name="",
                    x=tx,
                    y=ty,
                    weight=2)

    # Perform bjerrum calculations
    bx = list(titr.ph)
    bys = [list(alpha) for alpha in titr.alpha_analyte.T]

    # For every alpha value list, plot the alpha values at every pH and add the line to the plot
    for num, alpha in enumerate(bys):
        add_line_series(plot="bjerrum_plot",
                        name=f"species{num}",
                        x=bx,
                        y=alpha,
                        weight=2)


# Main gui formatting
with window("Main Window"):
    # Change the theme and make the text a little bigger.
    set_theme("Grey")
    set_global_font_scale(1.05)

    with tab_bar("Tab Bar"):
        with tab("Data Entry"):
            # Get the analyte data
            with group("Analyte", width=data_width):
                add_text("Analyte Data")
                add_input_text("Analyte Name", default_value="Citric Acid", callback=plot_callback)
                add_input_float("Analyte Concentration (M)", default_value=0.10, callback=plot_callback)
                add_input_text("Analyte pK value(s)", default_value="3.13, 4.76, 6.40", callback=plot_callback)
                add_input_float("Analyte Volume (mL)", default_value=25, callback=plot_callback)
                add_checkbox("Analyte is acidic", default_value=True, callback=plot_callback)
                add_checkbox("Analyte is strong", default_value=False, callback=plot_callback)

            # Add some spacing between the analyte and titrant data collection
            add_same_line()
            add_dummy(width=100)

            # Get the titrant data
            add_same_line()
            with group("Titrant", width=data_width):
                add_text("Titrant Data")
                add_input_text("Titrant Name", default_value="KOH", callback=plot_callback)
                add_input_float("Titrant Concentration (M)", default_value=0.10, callback=plot_callback)
                add_input_text("Titrant pK value(s)", default_value="0.20", callback=plot_callback)
                add_checkbox("Titrant is strong", default_value=True, callback=plot_callback)

            add_button("Plot data", callback=plot_callback, width=data_width * 2)

            # Put the titration curve under the data entry section
            add_next_column()
            with group("TitrationPlotGroup"):
                add_text("Titration Curve")
                add_plot("titration_plot", query_callback=query_titr, width=plot_width)

            # Put the bjerrum plot to the right of the titration curve
            add_same_line()
            with group("BjerrumPlotGroup"):
                add_text("Relative Species Plot")
                add_plot("bjerrum_plot", query_callback=query_bjer, width=plot_width)

            # TODO add file saving support. Both data and image.

        # Added a help placeholder
        with tab("Help"):
            add_text("This is where I plan on putting information which may be helpful to the user.")

        # Style tab for testing styles.
        with tab("Style Settings"):
            add_combo("Themes", items=themes, default_value="Dark", callback=apply_theme)
            add_slider_float("Font Size Multiplier", default_value=1.0, min_value=0.0, max_value=2.0,
                             callback=apply_text_multiplier)

# Run the curve.
start_dearpygui(primary_window="Main Window")

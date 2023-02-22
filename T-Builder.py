from webbrowser import open

import dearpygui.dearpygui as dpg
from matplotlib.pyplot import cm

import data_writing as dw
from titration_class import Compound, Titration

__author__ = "jkelowitt"
__version__ = "v2.3.4"
__license__ = "MIT"

LIMIT = 1000  # Actual limit to how many pKas you can have on each analyte/titrant
data_width = 200
color_map = cm.tab20


def _help(message):
    """
    Help message icon and hover over.
    Taken from: https://github.com/hoffstadt/DearPyGui/blob/master/dearpygui/demo.py
    """
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text("(?)", color=[0, 255, 0])
    with dpg.tooltip(t):
        dpg.add_text(message)


def open_link(sender, data):
    open("https://github.com/jkelowitt/t-builder", new=2)


def make_titration():
    # Create compounds
    Analyte = Compound(
        name=dpg.get_value("Analyte Name"),
        acidic=dpg.get_value("aa"),
        pKas=[float(i) for i in dpg.get_value("apk").split(",")],
    )

    Titrant = Compound(
        name=dpg.get_value("tname"),
        acidic=not dpg.get_value("aa"),
        pKas=[float(i) for i in dpg.get_value("tpk").split(",")],
    )

    # Create titration object
    titr = Titration(
        analyte=Analyte,
        titrant=Titrant,
        concentration_analyte=dpg.get_value("aconc"),
        concentration_titrant=dpg.get_value("tconc"),
        volume_analyte=dpg.get_value("avol"),
        decimal_places=dpg.get_value("precision"),
        temp=dpg.get_value("temperature"),
    )

    return titr


def plot_callback(sender, data):
    titr = make_titration()

    # Try to delete annotations if they're present
    # Need to be duplicated incase the number of e != number of b
    # Done to a limit in case the pKa count changes between callbacks
    # Ex. Going from trifunctional to monofunctional means that an intelligent range would only
    #   delete one of the three annotations.
    # Obligatory: This is terrible
    try:
        for n in range(LIMIT):
            dpg.delete_item(f"e{n}")
    except:
        pass
    try:
        for n in range(LIMIT):
            dpg.delete_item(f"b{n}")
    except:
        pass

    if dpg.get_value("plot_type") == "Speciation":
        # Wipe the plot, and relabel the axes
        dpg.delete_item("main_plot_y_axis")
        dpg.add_plot_axis(dpg.mvYAxis, tag="main_plot_y_axis", parent="main_plot")
        dpg.set_item_label("main_plot_x_axis", "pH")
        dpg.set_item_label("main_plot_y_axis", "Relative Speciation")
        dpg.set_item_label("main_plot", "Speciation Plot")
        dpg.bind_item_theme("main_plot", "speciation_theme")

        # Perform bjerrum calculations
        bx = list(titr.ph_full)
        bys = [list(alpha) for alpha in titr.alpha_analyte.T]

        # Plot the individual bjerrum calculations
        for num, alpha in enumerate(bys):
            dpg.add_line_series(bx, alpha, label=f"Species {num + 1}", parent="main_plot_y_axis")


    elif dpg.get_value("plot_type") == "Titration":
        # Perform titration calculations
        tx = list(titr.volume_titrant)
        ty = list(titr.ph)

        # Wipe the plot, and relabel the axes
        dpg.delete_item("main_plot_y_axis")
        dpg.add_plot_axis(dpg.mvYAxis, tag="main_plot_y_axis", parent="main_plot")
        dpg.set_item_label("main_plot_x_axis", "Volume (mL)")
        dpg.set_item_label("main_plot_y_axis", "pH")
        dpg.set_item_label("main_plot", "Titration Plot")

        # Plot the calculations
        dpg.add_line_series(tx, ty, label=f"Titration Curve", parent="main_plot_y_axis", tag="titration_curve")
        dpg.bind_item_theme("titration_curve", "titration_theme")

        # Plot special points over the curve
        # Offset annotations based on whether the annotations would collide with the line
        offset_tuple = (5, 5 * (1 if titr.analyte.acidic else -1))
        if dpg.get_value("buffer_regions"):
            vols, pHs = titr.find_buffer_points()
            vols = list(vols)

            dpg.add_scatter_series(vols, pHs, label="Buffer Points", parent="main_plot_y_axis", tag="buffer_points")
            dpg.bind_item_theme(f"buffer_points", "buffer_theme")

            # Add labels to the volumes of each point
            for n, (vol, pH) in enumerate(zip(vols, pHs)):
                # Annotations need to be above the line if the solution is basic to prevent the line from clipping
                dpg.add_plot_annotation(parent="main_plot", default_value=(vol, pH),
                                        label=f"{vol:.5g} mL", offset=offset_tuple, tag=f"b{n}")

        if dpg.get_value("equiv"):
            vols, pHs = titr.find_equiv_points()

            vols = list(vols)
            pHs = list(pHs)

            dpg.add_scatter_series(vols, pHs, parent="main_plot_y_axis", label="Equivalence Points", tag="equiv_points")
            dpg.bind_item_theme(f"equiv_points", "equiv_theme")

            # Add labels to the volumes of each point
            for n, (vol, pH) in enumerate(zip(vols, pHs)):
                # Annotations need to be above the line if the solution is basic to prevent the line from clipping
                dpg.add_plot_annotation(parent="main_plot", default_value=(vol, pH),
                                        label=f"{vol:.5g} mL", offset=offset_tuple, tag=f"e{n}")

        if dpg.get_value("1stderiv"):
            volume, pHderiv = titr.deriv(degree=1)
            data = titr._scale_data(pHderiv, dpg.get_value("1dscaler"))
            dpg.add_line_series(list(volume), list(data), parent="main_plot_y_axis", label="First Derivative",
                                tag="1stderivative")
            dpg.bind_item_theme("1stderivative", "yprime_theme")

        if dpg.get_value("2ndderiv"):
            volume, pHderiv = titr.deriv(degree=2)
            data = titr._scale_data(pHderiv, dpg.get_value("2dscaler"))
            dpg.add_line_series(list(volume), list(data), parent="main_plot_y_axis", label="Second Derivative",
                                tag="2ndderivative")
            dpg.bind_item_theme("2ndderivative", "yprimeprime_theme")

    # Auto fit axes to data
    dpg.fit_axis_data("main_plot_x_axis")
    dpg.fit_axis_data("main_plot_y_axis")


def save_titr_data(sender, data):
    titr = make_titration()
    title = f"{dpg.get_value('aname')}_{dpg.get_value('tname')}_titration".replace(" ", "_")
    dw.write_titration_data(titr, title=title)


def save_bjer_data(sender, data):
    titr = make_titration()
    title = f"{dpg.get_value('aname')}_{dpg.get_value('tname')}_species".replace(" ", "_")
    dw.write_alpha_data(titr, title=title)


def save_ana_data(sender, data):
    titr = make_titration()
    title = f"{dpg.get_value('aname')}_{dpg.get_value('tname')}_analysis".replace(" ", "_")
    dw.write_analysis_data(titr, title=title)


# Main gui formatting
dpg.create_context()

# Registry of all the values which the user interacts with
with dpg.value_registry():
    # Analyte values
    dpg.add_string_value(default_value="Citric Acid", tag="aname")
    dpg.add_float_value(default_value=0.10, tag="aconc")
    dpg.add_string_value(default_value="3.13, 4.76, 6.40", tag="apk")
    dpg.add_float_value(default_value=25, tag="avol")
    dpg.add_bool_value(default_value=True, tag="aa")

    # Titrant Values
    dpg.add_string_value(default_value="KOH", tag="tname")
    dpg.add_float_value(default_value=0.10, tag="tconc")
    dpg.add_string_value(default_value="14.76", tag="tpk")
    dpg.add_float_value(default_value=25, tag="tvol")

    # Experiment Values
    dpg.add_string_value(default_value="Titration", tag="plot_type")
    dpg.add_int_value(default_value=2, tag="precision")
    dpg.add_float_value(default_value=25.0, tag="temperature")
    dpg.add_bool_value(default_value=False, tag="buffer_regions")
    dpg.add_bool_value(default_value=False, tag="equiv")
    dpg.add_bool_value(default_value=False, tag="1stderiv")
    dpg.add_bool_value(default_value=False, tag="2ndderiv")
    dpg.add_float_value(default_value=8, tag="1dscaler")
    dpg.add_float_value(default_value=2, tag="2dscaler")

# Data series themes
with dpg.theme(tag="titration_theme"):
    with dpg.theme_component(dpg.mvLineSeries):
        # dpg.add_theme_color(dpg.mvPlotCol_Line, next(colors), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_Line, (0, 255, 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 3, category=dpg.mvThemeCat_Plots)

with dpg.theme(tag="speciation_theme"):
    with dpg.theme_component(dpg.mvLineSeries):
        # dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 0, 0), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 3, category=dpg.mvThemeCat_Plots)

with dpg.theme(tag="buffer_theme"):
    with dpg.theme_component(dpg.mvScatterSeries):
        dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 0, 0), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_MarkerSize, 5, category=dpg.mvThemeCat_Plots)

with dpg.theme(tag="equiv_theme"):
    with dpg.theme_component(dpg.mvScatterSeries):
        dpg.add_theme_color(dpg.mvPlotCol_Line, (0, 255, 0), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_MarkerSize, 5, category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_Marker, dpg.mvPlotMarker_Square, category=dpg.mvThemeCat_Plots)

with dpg.theme(tag="yprime_theme"):
    with dpg.theme_component(dpg.mvLineSeries):
        dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 0, 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 3, category=dpg.mvThemeCat_Plots)

with dpg.theme(tag="yprimeprime_theme"):
    with dpg.theme_component(dpg.mvLineSeries):
        dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 255, 0), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 3, category=dpg.mvThemeCat_Plots)

# Begin the actual gui formatting
with dpg.window(tag="PrimaryWindow"):
    with dpg.tab_bar(tag="Main Tab bar"):
        dpg.add_tab_button(label="T-Builder on GitHub", callback=open_link)

    with dpg.group(label="all", horizontal=True):
        with dpg.group(tag="Data Entry", horizontal=False, width=data_width):
            dpg.add_text("Plot To Show")
            dpg.add_radio_button(("Titration", "Speciation"), callback=plot_callback, horizontal=True,
                                 source="plot_type")

            dpg.add_text("Analyte Data")
            dpg.add_input_text(source="aname", label="Analyte Name", default_value="Citric Acid",
                               callback=plot_callback, )
            _help("Enter the name of the analyte. This is used when making the data files.")

            dpg.add_input_float(source="aconc", label="Analyte Concentration (M)", callback=plot_callback,
                                min_value=0, user_data=[0], )
            _help("Enter the concentration of the analyte in molarity.")

            dpg.add_input_text(source="apk", label="Analyte pKa value(s)", default_value="3.13, 4.76, 6.40",
                               callback=plot_callback, )
            _help("Enter the pKa values of the analyte. Separate them with commas if there are more than one.")

            dpg.add_input_float(source="avol", label="Analyte Volume (mL)", callback=plot_callback, user_data=[0],
                                min_value=0)
            _help("Enter the volume of the analyte in mL.")

            dpg.add_checkbox(source="aa", label="Analyte is Acidic", default_value=True, callback=plot_callback, )
            _help("Check this box if the analyte acts as an acid during this titration.")
            # TODO This may be automatable. Think "if pKa_a > pKa_t, then..."

            dpg.add_spacer(height=25)
            dpg.add_text("Titrant Data")

            dpg.add_input_text(source="tname", label="Titrant Name", default_value="KOH", callback=plot_callback, )
            _help("Enter the name of the titrant. This is used when naming the data files.")

            dpg.add_input_float(source="tconc", label="Titrant Concentration (M)", default_value=0.10,
                                min_value=0, callback=plot_callback, user_data=[0], )
            _help("Enter the concentration of the titrant in molarity.")

            dpg.add_input_text(source="tpk", label="Titrant pKa value(s)", default_value="14.76",
                               callback=plot_callback, )
            _help("Enter the pKa values of the titrant. Separate them with commas if there are more than one.")

            dpg.add_spacer(height=25)
            dpg.add_text("Titration Settings")

            dpg.add_input_int(source="precision", label="Number of Points", default_value=2, callback=plot_callback,
                              min_value=0, width=65, )
            _help("The number of pH points to calculate. (10^n items)")

            dpg.add_input_float(source="temperature", min_value=0, label="Temperature (C)", callback=plot_callback,
                                width=65, )
            _help("The temperature at which the titration occurs. (0 - 95 C)")

            dpg.add_spacer(height=25)
            dpg.add_text("Perform Titration Analysis")

            dpg.add_checkbox(label="Show Buffering Points", default_value=False, callback=plot_callback,
                             source="buffer_regions")
            _help("Show the center of the buffering regions on the Titration plot.")

            dpg.add_checkbox(label="Show Equivalence Points", default_value=False, callback=plot_callback,
                             source="equiv")
            _help("Show the equivalence points on the Titration plot.")

            dpg.add_checkbox(label="Show normalized y'", default_value=False, callback=plot_callback,
                             source="1stderiv")
            _help("Show the normalized 1st Derivative of the Titration plot")

            dpg.add_checkbox(label="Show normalized y''", default_value=False, callback=plot_callback,
                             source="2ndderiv")
            _help("Show the normalized 2nd Derivative of the Titration plot.")

            dpg.add_drag_float(label="Scale y'", default_value=8, min_value=0, speed=0.1, width=80, format="%0.2f",
                               callback=plot_callback, source="1dscaler")
            _help("Scale the 1st Derivative of the Titration plot.")

            dpg.add_drag_float(label="Scale y''", default_value=2, min_value=0, speed=0.1, width=80, format="%0.2f",
                               callback=plot_callback, source="2dscaler")
            _help("Scale the 2nd Derivative of the Titration plot.")

            dpg.add_spacer(height=25)
            dpg.add_text("Save Data to CSV")
            _help("All these save a csv file to the directory of the T-Builder.exe file.")
            dpg.add_button(label="Save Titration Data ", callback=save_titr_data)
            dpg.add_button(label="Save Speciation Data", callback=save_bjer_data)
            dpg.add_button(label="Save Analysis Data", callback=save_ana_data)

        # Put the titration curve under the data entry section
        with dpg.group(label="TitrationPlotGroup"):
            with dpg.plot(tag="main_plot"):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="Volume (mL)", tag="main_plot_x_axis")
                dpg.add_plot_axis(dpg.mvYAxis, label="pH", tag="main_plot_y_axis")

                # Plot the empty data, just load the plot in.
                dpg.add_line_series([], [], tag="main_plot_series", parent="main_plot_y_axis")

                # Auto fit axes to data
                dpg.fit_axis_data("main_plot_x_axis")
                dpg.fit_axis_data("main_plot_y_axis")

        # Set the plot themes
        dpg.bind_item_theme("main_plot_y_axis", "titration_theme")

    plot_callback("equiv", [])  # Make the plots appear on program start


def resize_plot():
    viewport_width = dpg.get_viewport_width()
    viewport_height = dpg.get_viewport_height()

    # The top bar, where the minimizze, expand, and close buttons are; are included in the viewport height
    HEIGHT_OF_TOP_BAR = 80

    # The grippable area around the window is also included, I think?
    WIDTH_BUFFER = 250

    tab_bar_height = dpg.get_item_height("Main Tab bar")
    data_entry_width = dpg.get_item_width("Data Entry")

    dpg.set_item_width("main_plot", viewport_width - data_width - WIDTH_BUFFER)
    dpg.set_item_height("main_plot", viewport_height - tab_bar_height - HEIGHT_OF_TOP_BAR)


# Run the curve.
if __name__ == "__main__":
    dpg.create_viewport(title="T-Builder")
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_viewport_resize_callback(resize_plot)
    dpg.set_primary_window("PrimaryWindow", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

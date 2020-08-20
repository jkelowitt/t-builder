"""Main and some sub guis"""

    Example: dpak2
    dp: Diprotic
    a: Acid
    k2: 2nd Dissociation Constant
"""

from guietta import Gui, ___, Exceptions, III, R, M, C

title = "<center style='font-size:20px'>"
big = "<u><center style='font-size:16px'>"
# Main Gui. Shows on startup.
gui = Gui(
    [M("plot")  , f"{title} Parameters"           , ___           ],
    [III        , f"{big} Titrant"                , ___           ],
    [III        , "Functionality:"                , "__tfunc__"   ],
    [III        , (C("Strong"), "tstrong")        , ___           ],
    [III        , (R("Acid"), "tacid")            , ___           ],
    [III        , f"{big} Analyte"                , ___           ],
    [III        , "Functionality:"                , "__afunc__"   ],
    [III        , (C("Strong"), "astrong")        , ___           ],
    [III        , (R("Acid"), "aacid")            , ___           ],
    [III        , (["Input Parameters"], "start") , ___           ],
    [III        , (["Save CSV"], "saveCSV")       , ___           ],
    [III        , (["Save Plot"], "savePlot")     , ___           ],
    exceptions=Exceptions.PRINT
    )


# Default Functionality
gui.tfunc = 1
gui.afunc = 1

save_fig_gui = Gui(
    ["Plot Save Name: ", "__figure_name__", ".png"],
    [["Save Plot"], ___, ___]
    )

save_fig_gui.title("Save Current Plot")

save_csv_gui = Gui(
    ["CSV Save Name: ", "__csv_name__", ".csv"],
    [["Save CSV"], ___, ___]
    )

save_fig_gui.title("Save Data to CSV")

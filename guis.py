"""
Sub GUI's for the main gui. Mainly for variable entry.

Parameter guide:
    The first two letters of each of the variables tells which functionality it is used for.
        mp: Monoprotic
        dp: Diprotic
        tp: Triprotic
    The third letter tells whether the variable pertains to an acid or base.
        a: acid
        b: base
    The remaining letters correlate to the literal variable name.
        n : Name
        k#: #th Dissociation Constant (If the # is absent, it is the first)
        c : Concentration
        v : Volume

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

dp_sb.title("Strong Base Titrant Diprotic")


# Triprotic Strong Acid Titrant
tp_sa = Gui(
    ["Base Name:"          , "__tpbn__"  ],
    ["Base Kb1:"           , "__tpbk1__" ],
    ["Base Kb2:"           , "__tpbk2__" ],
    ["Base Kb3:"           , "__tpbk3__" ],
    ["Base Concentration:" , "__tpbc__"  ],
    ["Base Volume (mL):"   , "__tpbv__"  ],
    ["Acid Name:"          , "__tpan__"  ],
    ["Acid Concentration:" , "__tpac__"  ],
    [Ok                    , ___         ],
    exceptions=Exceptions.PRINT
    )

tp_sa.title("Strong Acid Titrant Triprotic")

# Triprotic Strong Base Titrant
tp_sb = Gui(
    ["Acid Name:"          , "__tpan__"  ],
    ["Acid Ka1:"           , "__tpak1__" ],
    ["Acid Ka2:"           , "__tpak2__" ],
    ["Acid Ka3:"           , "__tpak3__" ],
    ["Acid Concentration:" , "__tpac__"  ],
    ["Acid Volume (mL):"   , "__tpav__"  ],
    ["Base Name:"          , "__tpbn__"  ],
    ["Base Concentration:" , "__tpbc__"  ],
    [Ok                    , ___         ],
    exceptions=Exceptions.PRINT
    )

tp_sb.title("Strong Base Titrant Triprotic")


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

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

from guietta import Gui, ___, Exceptions, R, Ok

# Monoprotic Sub Guis
mp_sa = Gui(
    ["The Base is:"        , R("Strong")   , R("Weak") ],
    ["Base Name:"          , "__mpbn__"    , ___       ],
    ["Base Kb:"            , "__mpbk__"    , ___       ],
    ["Base Concentration:" , "__mpbc__"    , ___       ],
    ["Base Volume (mL):"   , "__mpbv__"    , ___       ],
    ["Acid Name:"          , "__mpan__"    , ___       ],
    ["Acid Concentration:" , "__mpac__"    , ___       ],
    [Ok                    , ___           , ___       ],
    exceptions=Exceptions.PRINT
    )

mp_sa.title("Strong Acid Titrant")


mp_sb = Gui(
    ["The Acid is:"        , R("Strong")   , R("Weak") ],
    ["Acid Name:"          , "__mpan__"    , ___       ],
    ["Acid Ka:"            , "__mpak__"    , ___       ],
    ["Acid Concentration:" , "__mpac__"    , ___       ],
    ["Acid Volume (mL):"   , "__mpav__"    , ___       ],
    ["Base Name:"          , "__mpbn__"    , ___       ],
    ["Base Concentration:" , "__mpbc__"    , ___       ],
    [Ok                    , ___           , ___       ],
    exceptions=Exceptions.PRINT
    )

mp_sb.title("Strong Base Titrant")


# Diprotic Sub Guis
dp_sa = Gui(
    ["Base Name:"          , "__dpbn__"  ],
    ["Base Kb1:"           , "__dpbk1__" ],
    ["Base Kb2:"           , "__dpbk2__" ],
    ["Base Concentration:" , "__dpbc__"  ],
    ["Base Volume (mL):"   , "__dpbv__"  ],
    ["Acid Name:"          , "__dpan__"  ],
    ["Acid Concentration:" , "__dpac__"  ],
    [Ok                    , ___         ],
    exceptions=Exceptions.PRINT
    )

dp_sa.title("Strong Acid Titrant Diprotic")


dp_sb = Gui(
    ["Acid Name:"          , "__dpan__"   ],
    ["Acid Ka1:"           , "__dpak1__"  ],
    ["Acid Ka2:"           , "__dpak2__"  ],
    ["Acid Concentration:" , "__dpac__"   ],
    ["Acid Volume (mL):"   , "__dpav__"   ],
    ["Base Name:"          , "__dpbn__"   ],
    ["Base Concentration:" , "__dpbc__"   ],
    [Ok                    , ___          ],
    exceptions=Exceptions.PRINT
    )

dp_sb.title("Strong Base Titrant Diprotic")


# Triprotic Sub Guis
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


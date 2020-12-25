import titration_class as ts

"""Titrants"""
# Acids
HCl = ts.Titrant(name="HCl",
                 concentration=0.10,
                 acidic=True,
                 pK=[-6.5],
                 strong=True,
                 )

HI = ts.Titrant(name="HI",
                concentration=0.10,
                acidic=True,
                pK=[-10],
                strong=True)

HNO3 = ts.Titrant(name="HNO3",
                  concentration=0.10,
                  acidic=True,
                  pK=[-1.4],
                  strong=True)

# Bases
KOH = ts.Titrant(name="KOH",
                 concentration=0.10,
                 acidic=False,
                 pK=[0.5],
                 strong=True)

LiOH = ts.Titrant(name="LiOH",
                  concentration=0.10,
                  acidic=False,
                  pK=[-0.36],
                  strong=True)

NaOH = ts.Titrant(name="NaOH",
                  concentration=0.10,
                  acidic=False,
                  pK=[0.2],
                  strong=True)

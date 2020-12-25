import titration_class as ts

"""Strong Compounds"""
# Acids
HCl = ts.Compound(name="HCl",
                  acidic=True,
                  pKs=[-6.5],
                  strong=True,
                  )

HI = ts.Compound(name="HI",
                 acidic=True,
                 pKs=[-10],
                 strong=True)

HNO3 = ts.Compound(name="HNO3",
                   acidic=True,
                   pKs=[-1.4],
                   strong=True)

# Bases
KOH = ts.Compound(name="KOH",
                  acidic=False,
                  pKs=[0.5],
                  strong=True)

LiOH = ts.Compound(name="LiOH",
                   acidic=False,
                   pKs=[-0.36],
                   strong=True)

NaOH = ts.Compound(name="NaOH",
                   acidic=False,
                   pKs=[0.2],
                   strong=True)

"""Weak Compounds"""

# Acids
EDTA = ts.Compound(name="EDTA",
                   acidic=True,
                   pKs=[2.0, 2.7, 6.16, 10.26],
                   strong=False)

citric = ts.Compound(name="Citric Acid",
                     acidic=True,
                     pKs=[3.13, 4.76, 6.40],
                     strong=False)

carbonic = ts.Compound(name="Carbonic Acid",
                       acidic=True,
                       pKs=[6.37, 10.25],
                       strong=False)

H2S = ts.Compound(name="Hydrogen Sulfide",
                  acidic=True,
                  pKs=[7.04, 11.96],
                  strong=False)

oxalic = ts.Compound(name="Oxalic Acid",
                     acidic=True,
                     pKs=[1.25, 4.27],
                     strong=False)

phenol = ts.Compound(name="Phenol",
                     acidic=True,
                     pKs=[9.89],
                     strong=False)

phosphoric = ts.Compound(name="Phosphoric Acid",
                         acidic=True,
                         pKs=[2.15, 7.20, 12.35],
                         strong=False)

acetic = ts.Compound(name="Acetic Acid",
                     acidic=True,
                     pKs=[4.75],
                     strong=False)

ammonium = ts.Compound(name="Phenol",
                       acidic=True,
                       pKs=[9.2],
                       strong=False)

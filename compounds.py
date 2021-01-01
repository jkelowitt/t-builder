import titration_class as ts

acidic_water = ts.Compound(name="Water", acidic=True, pKs=[14.0], strong=False)
basic_water = ts.Compound(name="Water", acidic=False, pKs=[14.0], strong=False)

"""Strong Compounds"""
# Acids
HCl = ts.Compound(name="HCl", acidic=True, pKs=[-6.5], strong=True)
HI = ts.Compound(name="HI", acidic=True, pKs=[-10], strong=True)
HNO3 = ts.Compound(name="HNO3", acidic=True, pKs=[-1.4], strong=True)

# Bases
KOH = ts.Compound(name="KOH", acidic=False, pKs=[0.5], strong=True)
LiOH = ts.Compound(name="LiOH", acidic=False, pKs=[-0.36], strong=True)
NaOH = ts.Compound(name="NaOH", acidic=False, pKs=[0.2], strong=True)

"""Weak Compounds"""

# Acids
EDTA = ts.Compound(name="EDTA", acidic=True, pKs=[0.0, 1.5, 2.00, 2.69, 6.13, 10.37], strong=False)  # Pg 268 QCA
citric = ts.Compound(name="Citric Acid", acidic=True, pKs=[3.13, 4.76, 6.40], strong=False)
carbonic = ts.Compound(name="Carbonic Acid", acidic=True, pKs=[6.37, 10.25], strong=False)
acetic = ts.Compound(name="Acetic Acid", acidic=True, pKs=[4.75], strong=False)
ammonium = ts.Compound(name="Phenol", acidic=True, pKs=[9.2], strong=False)

# Bases
ammonia = ts.Compound(name="ammonia", acidic=False, pKs=[4.75], strong=False)
calcium_hydroxide = ts.Compound(name="calcium_hydroxide", acidic=False, pKs=[1.4, 2.43], strong=False)
methylamine = ts.Compound(name="methylamine", acidic=False, pKs=[3.36], strong=False)
ethylamine = ts.Compound(name="ethylamine", acidic=False, pKs=[3.25], strong=False)
aniline = ts.Compound(name="aniline", acidic=False, pKs=[9.4], strong=False)

# Lists of compound
basic_titrants = [KOH, NaOH, LiOH]
acidic_analytes = [EDTA, citric, carbonic, acetic, ammonium]
acidic_titrants = [HCl, HNO3, HI]
basic_analytes = [ammonia, calcium_hydroxide, methylamine, ethylamine, aniline]

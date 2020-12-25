import titration_class as ts

"""Analytes"""
# Acids
EDTA = ts.Analyte(name="EDTA",
                  concentration=0.10,
                  acidic=True,
                  pK=[2.0, 2.7, 6.16, 10.26],
                  strong=False,
                  volume=25)

citric = ts.Analyte(name="Citric Acid",
                    concentration=0.10,
                    acidic=True,
                    pK=[3.13, 4.76, 6.40],
                    strong=False,
                    volume=25)

carbonic = ts.Analyte(name="Carbonic Acid",
                      concentration=0.10,
                      acidic=True,
                      pK=[6.37, 10.25],
                      strong=False,
                      volume=25)

H2S = ts.Analyte(name="Hydrogen Sulfide",
                 concentration=0.10,
                 acidic=True,
                 pK=[7.04, 11.96],
                 strong=False,
                 volume=25)

oxalic = ts.Analyte(name="Oxalic Acid",
                    concentration=0.10,
                    acidic=True,
                    pK=[1.25, 4.27],
                    strong=False,
                    volume=25)

phenol = ts.Analyte(name="Phenol",
                    concentration=0.10,
                    acidic=True,
                    pK=[9.89],
                    strong=False,
                    volume=25)

phosphoric = ts.Analyte(name="Phosphoric Acid",
                        concentration=0.10,
                        acidic=True,
                        pK=[2.15, 7.20, 12.35],
                        strong=False,
                        volume=25)

acetic = ts.Analyte(name="Acetic Acid",
                    concentration=0.10,
                    acidic=True,
                    pK=[4.75],
                    strong=False,
                    volume=25)

ammonium = ts.Analyte(name="Phenol",
                      concentration=0.10,
                      acidic=True,
                      pK=[9.2],
                      strong=False,
                      volume=25)
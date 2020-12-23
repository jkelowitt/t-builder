from titration_class import Titration

"""Acid Analytes"""

# Strong Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
a = Titration(analyte_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[-6],
              pkt_values=[-6],
              strong_analyte=True,
              strong_titrant=True)

# Weak Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
b = Titration(analyte_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[6],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

# Weak Diprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
c = Titration(analyte_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

# Weak Triprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
d = Titration(analyte_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 6, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

# Weak Monoprotic Acidic Analyte, Weak Monofunctional Basic Titrant.
e = Titration(analyte_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[7],
              pkt_values=[5],
              strong_analyte=False,
              strong_titrant=False)

# EDTA Analyte, KOH Basic Titrant.
f = Titration(analyte_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[2.0, 2.7, 6.16, 10.26],
              pkt_values=[0.2],
              strong_analyte=False,
              strong_titrant=True)

"""Base Analytes"""

# Strong Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
g = Titration(analyte_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[-6],
              pkt_values=[-6],
              strong_analyte=True,
              strong_titrant=True)

# Weak Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
h = Titration(analyte_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[6],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

# Weak Difunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
i = Titration(analyte_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

# Weak Trifunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
j = Titration(analyte_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 6, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

# Weak Monofunctional Basic Analyte, Weak Monoprotic Acidic Titrant.
k = Titration(analyte_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[7],
              pkt_values=[5],
              strong_analyte=False,
              strong_titrant=False)

# EDTA ion Analyte, HCl Acid Titrant.
l = Titration(analyte_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[2.0, 2.7, 6.16, 10.26],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

tests = [a, b, c, d, e, f, g, h, i, j, k, l]

for num, test in enumerate(tests):
    # test.plot_titration_curve("Titration Curve")
    # test.plot_alpha_curve("Alpha Curve")
    # test.write_alpha_data(f"test#{num}")
    # test.write_titration_data(f"test#{num}")
    pass

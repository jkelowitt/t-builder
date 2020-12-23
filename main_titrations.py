from titration_class import Titration

"""Acid Analytes"""
# Strong Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
a = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[-6],
              pkt_values=[-6],
              strong_analyte=True,
              strong_titrant=True,
              title="Strong Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant")

# Weak Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
b = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[6],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.")

# Weak Diprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
c = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Diprotic Acidic Analyte, Strong Monoprotic Basic Titrant.")

# Weak Triprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
d = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 6, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Triprotic Acidic Analyte, Strong Monoprotic Basic Titrant.")

# Weak Monoprotic Acidic Analyte, Weak Monofunctional Basic Titrant.
e = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[7],
              pkt_values=[5],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Monoprotic Acidic Analyte, Weak Monofunctional Basic Titrant.")

# Weak Polyprotic Acidic Analyte, Weak Polyfunctional Basic Titrant.
f = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 4.5, 5, 6, 7.23, 8, 9, 10, 11, 12],
              pkt_values=[3, 4.5, 5, 6, 7, 8, 9, 10, 11, 12],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Polyprotic Acidic Analyte, Weak Polyfunctional Basic Titrant.")

"""Base Analytes"""

# Strong Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
g = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[-6],
              pkt_values=[-6],
              strong_analyte=True,
              strong_titrant=True,
              title="Strong Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")

# Weak Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
h = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[6],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")

# Weak Difunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
i = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Difunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")

# Weak Trifunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
j = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 6, 9],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Trifunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")

# Weak Monofunctional Basic Analyte, Weak Monoprotic Acidic Titrant.
k = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[7],
              pkt_values=[5],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Monofunctional Basic Analyte, Weak Monoprotic Acidic Titrant.")

# Weak Polyfunctional Base Analyte, Weak Polyprotic Acid Titrant.
l = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 4.5, 5, 6, 7.23, 8, 9, 10, 11, 12],
              pkt_values=[3, 4.5, 5, 6, 7, 8, 9, 10, 11, 12],
              strong_analyte=False,
              strong_titrant=True,
              title="Weak Polyfunctional Base Analyte, Weak Polyprotic Acid Titrant.")

tests = [a, b, c, d, e, f, g, h, i, j, k, l]

for test in tests:
    test.plot_titration_curve()
    # test.plot_alpha_curve()

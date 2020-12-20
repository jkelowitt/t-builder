from titration_class import Titration

# Strong Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
# TODO figure out why strong-strong is giving two straight lines instead of a perfect cross
a = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[1000],
              pkt_values=[1000],
              title="Strong Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant")
a.plot_titration_curve()

# Weak Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
a = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[6],
              pkt_values=[1000],
              title="Weak Monoprotic Acidic Analyte, Strong Monoprotic Basic Titrant.")
a.plot_titration_curve()

# Weak Diprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
a = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 9],
              pkt_values=[1000],
              title="Weak Diprotic Acidic Analyte, Strong Monoprotic Basic Titrant.")
a.plot_titration_curve()

# Weak Triprotic Acidic Analyte, Strong Monoprotic Basic Titrant.
a = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 6, 9],
              pkt_values=[1000],
              title="Weak Triprotic Acidic Analyte, Strong Monoprotic Basic Titrant.")
a.plot_titration_curve()

# Strong Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
a = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[1000],
              pkt_values=[1000],
              title="Strong Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")
a.plot_titration_curve()

# Weak Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
a = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[6],
              pkt_values=[1000],
              title="Weak Monofunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")
a.plot_titration_curve()

# Weak Difunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
a = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 9],
              pkt_values=[1000],
              title="Weak Difunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")
a.plot_titration_curve()

# Weak Trifunctional Basic Analyte, Strong Monoprotic Acidic Titrant.
a = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[3, 6, 9],
              pkt_values=[1000],
              title="Weak Trifunctional Basic Analyte, Strong Monoprotic Acidic Titrant.")
a.plot_titration_curve()

# Weak Monofunctional Basic Analyte, Weak Monoprotic Acidic Titrant.
a = Titration(analyte_is_acidic=False,
              titrant_is_acidic=True,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[7],
              pkt_values=[5],
              title="Weak Monofunctional Basic Analyte, Weak Monoprotic Acidic Titrant.")
a.plot_titration_curve()

# Weak Monoprotic Acidic Analyte, Weak Monofunctional Basic Titrant.
a = Titration(analyte_is_acidic=True,
              titrant_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[7],
              pkt_values=[5],
              title="Weak Monoprotic Acidic Analyte, Weak Monofunctional Basic Titrant.")
a.plot_titration_curve()

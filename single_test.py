from titration_class import Titration


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

a.plot_titration_curve()
a.plot_alpha_curve()
a.write_titration_data()
a.write_alpha_data()

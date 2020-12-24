from titration_class import Titration


# EDTA ion Analyte, HCl Acid Titrant.
a = Titration(analyte_is_acidic=False,
              volume_analyte=25,
              concentration_analyte=0.10,
              concentration_titrant=0.10,
              pka_values=[2.0, 2.7, 6.16, 10.26],
              pkt_values=[-6],
              strong_analyte=False,
              strong_titrant=True)

a.plot_titration_curve()
a.plot_alpha_curve()
a.write_titration_data()
a.write_alpha_data()

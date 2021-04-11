from titration_class import *
from compounds import *

titrations = []

for t in strong_acids:
    for a in weak_bases:
        titrations.append(
            Titration(analyte=a, titrant=t, concentration_analyte=0.10, concentration_titrant=0.10, volume_analyte=25)
        )

for t in strong_bases:
    for a in weak_acids:
        titrations.append(
            Titration(analyte=a, titrant=t, concentration_analyte=0.10, concentration_titrant=0.10, volume_analyte=25)
        )

for titr in titrations:
    titr.write_titration_data(
        title=f"{titr.analyte.name}_{titr.titrant.name}_titration_data".replace(" ", "_").lower(), file_headers=True
    )
    titr.write_alpha_data(
        title=f"{titr.analyte.name}_{titr.titrant.name}_alpha_data".replace(" ", "_").lower(), file_headers=True
    )
    titr.write_analysis_data(
        title=f"{titr.analyte.name}_{titr.titrant.name}_analysis_data".replace(" ", "_").lower(), file_headers=True
    )

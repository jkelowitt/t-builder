from titration_class import *
from compounds import *

titrations = []

for t in acidic_titrants:
    for a in basic_analytes:
        titrations.append(
            Titration(analyte=a, titrant=t, concentration_analyte=0.10, concentration_titrant=0.10, volume_analyte=25))

for t in basic_titrants:
    for a in acidic_analytes:
        titrations.append(
            Titration(analyte=a, titrant=t, concentration_analyte=0.10, concentration_titrant=0.10, volume_analyte=25))

for titr in titrations:
    titr.write_titration_data(title=f"test_data/{titr.aname}_{titr.tname}_titration_data".replace(" ", "_").lower(),
                              file_headers=True)
    titr.write_alpha_data(title=f"test_data/{titr.aname}_{titr.tname}_alpha_data".replace(" ", "_").lower(),
                          file_headers=True)
    titr.write_analysis_data(title=f"test_data/{titr.aname}_{titr.tname}_analysis_data".replace(" ", "_").lower(),
                             file_headers=True)

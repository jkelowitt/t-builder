from typing import List
from pandas import DataFrame
from numpy import transpose


def write_alpha_data(titr,
                     title: str = "Alpha Value Data",
                     file_headers: bool = True,
                     species_names: List[str] = None) -> None:

    """Write the numerical alpha value data to a csv file."""

    # Initialize the dataframe with the ph values
    data_dict = {"pH": titr.ph}

    # Add the alpha values for each analyte species
    if species_names is None:  # If names are not specified, just use generics.
        for num, alpha in enumerate(transpose(titr.alpha_analyte)):
            data_dict[f"alpha{num}"] = alpha
    else:  # If names are specified, use them.
        for num, alpha in enumerate(transpose(titr.alpha_analyte)):
            try:  # TODO What if too many names?
                data_dict[species_names[num]] = alpha
            except IndexError:  # TODO should just put in place holders names into the species labels
                raise ValueError("You have not supplied enough species names!")

    # Make and write the data frame to a csv
    data = DataFrame(data_dict)
    data.to_csv(f"{title}.csv", index=False, header=file_headers)


def write_titration_data(titr, title: str = "Titration Curve Data", file_headers: bool = True) -> None:
    """Write the volume and pH value for the titration to a csv file."""
    # Make dataframe.
    pH, volume = titr.trim_values(titr.ph, titr.volume_titrant)
    data = DataFrame({"volume": volume, "pH": pH})

    # Write to a csv.
    data.to_csv(f"{title}.csv", index=False, header=file_headers)


def write_analysis_data(titr, title: str = "Analysis Data", file_headers: bool = True) -> None:
    """Write all the data relating to the titration, and its analysis to a csv file."""
    # Make dataframe.
    pH, volume = titr.trim_values(titr.ph, titr.volume_titrant)
    volumeD1, deriv1 = titr.deriv(1)
    volumeD2, deriv2 = titr.deriv(2)
    volumeEq, pHEq = titr.find_equiv_points()
    volumeBf, pHBf = titr.find_buffer_points()

    # Label the analysis rows
    analysis_row_labels = [
        *[f"eq pt {n}" for n in range(1, len(volumeEq) + 1)],
        *[f"bf pt {n}" for n in range(1, len(volumeBf) + 1)],
    ]

    # Input data to the analysis columns
    analysis_volumes = [*[n for n in volumeEq], *[n for n in volumeBf]]
    analysis_pHs = [*[n for n in pHEq], *[n for n in pHBf]]

    # Add spacers so that the Dataframe doesn't throw a fit
    while len(analysis_row_labels) < len(deriv1):
        analysis_row_labels.append(None)
        analysis_volumes.append(None)
        analysis_pHs.append(None)

    # Add the data to the dataframe.
    data = DataFrame(
        {
            "volume": volume,
            "pH": pH,
            "1st Derivative": deriv1,
            "2nd Derivative": deriv2,
            " ": [" " for _ in range(len(deriv1))],  # Spacer column
            "Analysis": analysis_row_labels,
            "Volume at Point": analysis_volumes,
            "pH at Point": analysis_pHs,
        }
    )

    # Write to a csv.
    data.to_csv(f"{title}.csv", header=file_headers, index=False)

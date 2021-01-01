import unittest
from titration_class import *
import os
import pandas as pd
from compounds import *


class TestTitrationClassModule(unittest.TestCase):
    def setUp(self):
        self.titrations = []

        for t in acidic_titrants:
            for a in basic_analytes:
                self.titrations.append(Titration(a, t, 0.10, 0.10, 25))

        for t in basic_titrants:
            for a in acidic_analytes:
                self.titrations.append(Titration(a, t, 0.10, 0.10, 25))

    def test_first_derivative_can_be_made(self):
        for titration in self.titrations:
            self.assertIsNotNone(titration.deriv(1))

    def test_first_derivative_volume_size_is_correct(self):
        for titration in self.titrations:
            volume, derivative = array(titration.deriv(1))
            self.assertEqual(len(volume), len(titration.ph_t))

    """Second Derivative Tests"""

    def test_second_derivative_can_be_made(self):
        for titration in self.titrations:
            self.assertIsNotNone(titration.deriv(2))

    def test_second_derivative_volume_size_is_correct(self):
        for titration in self.titrations:
            volume, derivative = array(titration.deriv(2))
            self.assertEqual(len(volume), len(titration.volume_titrant_t))

    """File Tests"""

    def test_titration_file_can_be_made(self):
        for titration in self.titrations:
            titration.write_titration_data()
            self.assertTrue(os.path.exists("Titration Curve Data.csv"))
            os.remove("Titration Curve Data.csv")

    def test_relative_species_file_can_be_made(self):
        for titration in self.titrations:
            titration.write_alpha_data()
            self.assertTrue(os.path.exists("Alpha Value Data.csv"))
            os.remove("Alpha Value Data.csv")

    def test_titration_file_has_data(self):
        for titration in self.titrations:
            titration.write_titration_data(file_headers=True)
            data = pd.read_csv("Titration Curve Data.csv")
            self.assertIsNotNone(data.head())
            os.remove("Titration Curve Data.csv")

    def test_relative_species_file_has_data(self):
        for titration in self.titrations:
            titration.write_alpha_data(file_headers=True)
            data = pd.read_csv("Alpha Value Data.csv")
            self.assertIsNotNone(data.head())
            os.remove("Alpha Value Data.csv")

    def test_titration_file_has_correct_data(self):
        for titration in self.titrations:
            titration.write_titration_data(file_headers=True)
            data = pd.read_csv("Titration Curve Data.csv")
            check = pd.read_csv(
                f"test_data/{titration.aname}_{titration.tname}_titration_data.csv".replace(
                    " ", "_"
                ).lower()
            )
            self.assertSequenceEqual(
                data.head().to_dict(), check.head().to_dict(), seq_type=dict
            )

            os.remove("Titration Curve Data.csv")

    def test_relative_species_file_has_correct_data(self):
        for titration in self.titrations:
            titration.write_alpha_data(file_headers=True)
            data = pd.read_csv("Alpha Value Data.csv")
            check = pd.read_csv(
                f"test_data/{titration.aname}_{titration.tname}_alpha_data.csv".replace(
                    " ", "_"
                ).lower()
            )
            self.assertSequenceEqual(
                data.head().to_dict(), check.head().to_dict(), seq_type=dict
            )

            os.remove("Alpha Value Data.csv")

    """Value checks"""

    def test_values_have_same_length(self):
        for titration in self.titrations:

            untrimmed = [
                titration.volume_titrant,
                titration.ph,
                titration.hydronium,
                titration.hydroxide,
                titration.alpha_analyte,
            ]
            length = len(untrimmed[0])
            for value in untrimmed:
                self.assertEqual(
                    len(value),
                    length,
                )

    def test_trimmed_values_have_same_length(self):
        for titration in self.titrations:
            trimmed = titration.trim_values(
                titration.volume_titrant,
                titration.ph,
                titration.hydronium,
                titration.hydroxide,
                titration.alpha_analyte,
            )
            length = len(next(trimmed))
            for value in trimmed:
                self.assertEqual(len(value), length)

    def test_trimmed_values_have_less_values_than_untrimmed_values(self):
        for titration in self.titrations:
            trimmed = titration.trim_values(
                titration.volume_titrant,
                titration.ph,
                titration.hydronium,
                titration.hydroxide,
                titration.alpha_analyte,
            )
            untrimmed = [
                titration.volume_titrant,
                titration.ph,
                titration.hydronium,
                titration.hydroxide,
                titration.alpha_analyte,
            ]

            for trim in trimmed:
                for untrim in untrimmed:
                    self.assertTrue(len(trim) <= len(untrim))

    """Functions Check"""

    def test_scaled_data_less_than_one(self):
        for titration in self.titrations:
            scaled = titration.scale_data(titration.ph, 1)
            for scale in scaled:
                self.assertTrue(scale <= 1)

    def test_alpha_index_scaling(self):
        test_list = [[5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]]
        f = self.titrations[0].scale_alphas(test_list)
        for sl in f:
            self.assertSequenceEqual(list(sl), [0, 4, 6, 6, 4])


if __name__ == "__main__":
    unittest.main()

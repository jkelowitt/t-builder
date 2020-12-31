"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import unittest
from titration_class import *
import os
import pandas as pd


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        # Make the analyte
        self.analyte = Compound(
            name="Citric Acid", acidic=True, pKs=[3.13, 4.76, 6.40], strong=False
        )

        # Make the titrant
        self.titrant = Compound(name="LiOH", acidic=False, pKs=[-0.36], strong=True)

        # Create the titration curve for testing.
        self.titration = Titration(
            analyte=self.analyte,
            titrant=self.titrant,
            concentration_analyte=0.10,
            concentration_titrant=0.10,
            volume_analyte=25,
        )

    def test_compound_values_transferred_to_titration_object(self):
        # Check acidity
        self.assertEqual(self.titration.analyte_is_acidic, self.analyte.acidic)
        self.assertEqual(self.titration.titrant_acidity, self.titrant.acidic)

        # Check strength
        self.assertEqual(self.titration.strong_analyte, self.analyte.strong)
        self.assertEqual(self.titration.strong_titrant, self.titrant.strong)

        # Check pK values
        self.assertEqual(self.titration.pk_analyte, self.analyte.pKs)
        self.assertEqual(self.titration.pk_titrant, self.titrant.pKs)

    def test_equivalence_points_correct(self):
        vols, pHs = self.titration.find_equiv_points()

        # Check the volumes
        self.assertSequenceEqual(
            list(vols), [25.032335898041598, 49.97742720475134, 75.00043327034554]
        )

        # Check the pHs
        self.assertSequenceEqual(list(pHs), [3.95, 5.58, 9.40], seq_type=list)

    def test_buffer_points_correct(self):
        vols, pKas = self.titration.find_buffer_points()

        # Check the volumes
        self.assertSequenceEqual(
            list(vols), [12.655691304269071, 37.479364100284926, 62.074624622098824]
        )

        # Check the pHs
        self.assertSequenceEqual(list(pKas), [3.13, 4.76, 6.40], seq_type=list)

    def test_first_derivative_can_be_made(self):
        self.assertIsNotNone(self.titration.deriv(1))

    def test_first_derivative_volume_size_is_correct(self):
        volume, derivative = array(self.titration.deriv(1))
        self.assertEqual(len(volume), 1021)

    def test_first_derivative_peak_location_is_correct(self):
        volume, derivative = array(self.titration.deriv(1))
        max_derivative = max(derivative)
        self.assertEqual(where(derivative == max_derivative)[0][0], 731)

    """Second Derivative Tests"""

    def test_second_derivative_can_be_made(self):
        self.assertIsNotNone(self.titration.deriv(2))

    def test_second_derivative_volume_size_is_correct(self):
        volume, derivative = array(self.titration.deriv(2))
        self.assertEqual(len(volume), 1021)

    def test_second_derivative_peak_location_is_correct(self):
        volume, derivative = array(self.titration.deriv(2))
        max_derivative = max(derivative)
        self.assertEqual(where(derivative == max_derivative)[0][0], 702)

    def test_titration_file_can_be_made(self):
        self.titration.write_titration_data()
        self.assertTrue(os.path.exists("Titration Curve Data.csv"))
        os.remove("Titration Curve Data.csv")

    def test_relative_species_file_can_be_made(self):
        self.titration.write_alpha_data()
        self.assertTrue(os.path.exists("Alpha Value Data.csv"))
        os.remove("Alpha Value Data.csv")

    def test_titration_file_has_data(self):
        self.titration.write_titration_data(file_headers=True)
        data = pd.read_csv("Titration Curve Data.csv")
        self.assertIsNotNone(data.head())
        os.remove("Titration Curve Data.csv")

    def test_relative_species_file_has_data(self):
        self.titration.write_alpha_data(file_headers=True)
        data = pd.read_csv("Alpha Value Data.csv")
        self.assertIsNotNone(data.head())
        os.remove("Alpha Value Data.csv")

    def test_titration_file_has_correct_data(self):
        self.titration.write_titration_data(file_headers=True)
        data = pd.read_csv("Titration Curve Data.csv")
        check = pd.read_csv("test_data/Citric_acid_LiOH_titration.csv")
        self.assertSequenceEqual(
            data.head().to_dict(), check.head().to_dict(), seq_type=dict
        )

        os.remove("Titration Curve Data.csv")

    def test_relative_species_file_has_correct_data(self):
        self.titration.write_alpha_data(file_headers=True)
        data = pd.read_csv("Alpha Value Data.csv")
        check = pd.read_csv("test_data/Citric_acid_LiOH_bjerrum.csv")
        self.assertSequenceEqual(
            data.head().to_dict(), check.head().to_dict(), seq_type=dict
        )
        os.remove("Alpha Value Data.csv")

    def test_values_have_same_length(self):
        untrimmed = [
            self.titration.volume_titrant,
            self.titration.ph,
            self.titration.hydronium,
            self.titration.hydroxide,
            self.titration.alpha_analyte,
        ]

        for value in untrimmed:
            self.assertEqual(
                len(value),
                1401,
            )

    def test_trimmed_values_have_same_length(self):
        trimmed = self.titration.trim_values(
            self.titration.volume_titrant,
            self.titration.ph,
            self.titration.hydronium,
            self.titration.hydroxide,
            self.titration.alpha_analyte,
        )
        for value in trimmed:
            self.assertEqual(
                len(value),
                1021,
            )

    def test_trimmed_values_have_less_values_than_untrimmed_values(self):
        trimmed = self.titration.trim_values(
            self.titration.volume_titrant,
            self.titration.ph,
            self.titration.hydronium,
            self.titration.hydroxide,
            self.titration.alpha_analyte,
        )
        untrimmed = [
            self.titration.volume_titrant,
            self.titration.ph,
            self.titration.hydronium,
            self.titration.hydroxide,
            self.titration.alpha_analyte,
        ]

        for trim in trimmed:
            for untrim in untrimmed:
                self.assertTrue(len(trim) <= len(untrim))

    def test_scaled_data_less_than_one(self):
        test_data = [1, 0.00000002, -10, 1e256, -0.0, 0.0]
        scaled = self.titration.scale_data(test_data, 6)
        for scale, datum in zip(scaled, test_data):
            self.assertTrue(scale <= 6)


if __name__ == "__main__":
    unittest.main()

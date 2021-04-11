from unittest import TestCase, main
from titration_class import array, Titration, scale_data
from compounds import strong_acids, strong_bases, weak_acids, weak_bases


class TestTitrationClassModule(TestCase):
    def setUp(self):
        self.titrations = []

        for t in strong_acids:
            for a in weak_bases:
                self.titrations.append(
                    Titration(
                        analyte=a, titrant=t, volume_analyte=25, concentration_titrant=0.10, concentration_analyte=0.10
                    )
                )

        for t in strong_bases:
            for a in weak_acids:
                self.titrations.append(
                    Titration(
                        analyte=a, titrant=t, volume_analyte=25, concentration_titrant=0.10, concentration_analyte=0.10
                    )
                )

    """First Derivative Tests"""

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

    # """File Tests"""  This takes too long. Involves the process of creating >450 MB of data. Consolidate later.
    #
    # def test_titration_file_can_be_made(self):
    #     for titration in self.titrations:
    #         titration.write_titration_data()
    #         self.assertTrue(path.exists("Titration Curve Data.csv"))
    #         remove("Titration Curve Data.csv")
    #
    # def test_relative_species_file_can_be_made(self):
    #     for titration in self.titrations:
    #         titration.write_alpha_data()
    #         self.assertTrue(path.exists("Alpha Value Data.csv"))
    #         remove("Alpha Value Data.csv")
    #
    # def test_titration_file_has_data(self):
    #     for titration in self.titrations:
    #         titration.write_titration_data(file_headers=True)
    #         data = read_csv("Titration Curve Data.csv")
    #         self.assertIsNotNone(data.head())
    #         remove("Titration Curve Data.csv")
    #
    # def test_relative_species_file_has_data(self):
    #     for titration in self.titrations:
    #         titration.write_alpha_data(file_headers=True)
    #         data = read_csv("Alpha Value Data.csv")
    #         self.assertIsNotNone(data.head())
    #         remove("Alpha Value Data.csv")
    #
    # def test_titration_file_has_correct_data(self):
    #     for titration in self.titrations:
    #         titration.write_titration_data(file_headers=True)
    #         data = read_csv("Titration Curve Data.csv")
    #         check = read_csv(
    #             f"test_data/{titration.aname}_{titration.tname}_titration_data.csv".replace(" ", "_").lower()
    #         )
    #         self.assertDictEqual(data.to_dict(), check.to_dict())
    #
    #         remove("Titration Curve Data.csv")
    #
    # def test_relative_species_file_has_correct_data(self):
    #     for titration in self.titrations:
    #         titration.write_alpha_data(file_headers=True)
    #         data = read_csv("Alpha Value Data.csv")
    #         check = read_csv(f"test_data/{titration.aname}_{titration.tname}_alpha_data.csv".replace(" ", "_").lower())
    #         self.assertDictEqual(data.head().to_dict(), check.head().to_dict())
    #
    #         remove("Alpha Value Data.csv")
    #
    # def test_analysis_file_has_correct_data(self):
    #     for titration in self.titrations:
    #         titration.write_analysis_data(file_headers=True)
    #         data = read_csv("Analysis Data.csv")
    #         check = read_csv(
    #             f"test_data/{titration.aname}_{titration.tname}_analysis_data.csv".replace(" ", "_").lower()
    #         )
    #
    #         self.assertDictEqual(data.head(2).to_dict(), check.head(2).to_dict())
    #
    #         remove("Analysis Data.csv")

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
            scaled = scale_data(titration.ph, 1)
            for scale in scaled:
                self.assertTrue(scale <= 1)

    def test_alpha_index_scaling(self):
        test_list = array([[5, 4, 3, 2, 1] for _ in range(200)])
        f = self.titrations[0].scale_alphas(test_list)
        for sl in f:
            self.assertSequenceEqual(list(sl), [0, 4, 6, 6, 4])


if __name__ == "__main__":
    main()

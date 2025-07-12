
"""
Unit tests for student analyzer project
"""

import unittest
from step2_calculate_average import calculate_averages
from step3_calculate_median import calculate_median_score
from step4_calculate_mode import calculate_mode_score
from step5_calculate_range import calculate_range_score
from step6_variance_std import calculate_dispersion

class TestStudentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.students = [
            {"name": "Ali", "scores": [15, 18, 19]},
            {"name": "Sara", "scores": [10, 12, 14]},
            {"name": "Nima", "scores": [17, 16, 18]}
        ]
        self.updated = calculate_averages(self.students.copy())

    def test_calculate_averages(self):
        self.assertAlmostEqual(self.updated[0]["average"], 17.33, places=2)
        self.assertAlmostEqual(self.updated[1]["average"], 12.0)
        self.assertAlmostEqual(self.updated[2]["average"], 17.0)

    def test_median(self):
        med = calculate_median_score(self.updated)
        self.assertEqual(med, 17.0)

    def test_mode(self):
        mod = calculate_mode_score(self.updated)
        self.assertIn(mod, [17.0, "No unique mode"])

    def test_range(self):
        rng = calculate_range_score(self.updated)
        self.assertAlmostEqual(rng, 5.33, places=2)

    def test_dispersion(self):
        disp = calculate_dispersion(self.updated)
        self.assertIn("variance", disp)
        self.assertIn("std_dev", disp)
        self.assertGreater(disp["variance"], 0)
        self.assertGreater(disp["std_dev"], 0)

if __name__ == '__main__':
    unittest.main()

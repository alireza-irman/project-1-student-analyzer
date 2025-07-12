
"""
Step 8: Basic unit tests for Student Analyzer
"""

import unittest
from step2_calculate_average import calculate_averages

class TestStudentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"name": "Ali", "scores": [15, 18, 19]},
            {"name": "Sara", "scores": [10, 12, 14]}
        ]

    def test_calculate_averages(self):
        result = calculate_averages(self.sample.copy())
        self.assertEqual(result[0]["average"], 17.333333333333332)
        self.assertEqual(result[1]["average"], 12.0)

if __name__ == "__main__":
    unittest.main()

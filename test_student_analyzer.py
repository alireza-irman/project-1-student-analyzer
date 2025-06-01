import unittest
from statistics import mean, median, mode, variance, stdev

class TestStudentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.scores = [15.0, 18.0, 12.0, 19.0, 16.0]

    def test_mean(self):
        self.assertAlmostEqual(mean(self.scores), 16.0)

    def test_median(self):
        self.assertEqual(median(self.scores), 16.0)

    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_variance(self):
        self.assertAlmostEqual(variance(self.scores), 7.0)

    def test_std_dev(self):
        self.assertAlmostEqual(stdev(self.scores), 2.6457, places=3)

if __name__ == '__main__':
    unittest.main()

import unittest, math
from statistics import mean
from myscript import find_max, find_min, find_sum, find_prod, find_mean, data


class TestStringMethods(unittest.TestCase):
    def test_max(self):
        self.assertEqual(find_max(), max(data))

    def test_min(self):
        self.assertEqual(find_min(), min(data))

    def test_sum(self):
        self.assertEqual(find_sum(), sum(data))

    def test_prod(self):
        self.assertEqual(find_prod(), math.prod(data))

    def test_mean(self):
        self.assertEqual(find_mean(), mean(data))

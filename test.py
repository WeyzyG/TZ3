import unittest, math
from time import time
from statistics import mean
from myscript import find_max, find_min, find_sum, find_prod, find_mean, data

t_1 = time()


class SomeTest(unittest.TestCase):

    def test_max(self):
        self.assertEqual(find_max(), max())

    def test_min(self):
        self.assertEqual(find_min(), min(data))

    def test_sum(self):
        self.assertEqual(find_sum(), sum(data))

    def test_prod(self):
        self.assertEqual(find_prod(), math.prod(data))

    def test_mean(self):  # Дополнительный тест
        self.assertEqual(find_mean(), mean(data))


t_2 = time()
work_time = t_2 - t_1
print(f"Время: {work_time} сек.")

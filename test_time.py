import unittest
import time
from myscript import find_max, find_min, find_sum, find_prod, find_mean


class SomeTest(unittest.TestCase):
    def test_time(self):
        print('Время выполнения функций:')
        time_1 = time.time()
        find_max()
        print(f"find_max: {time.time() - time_1} sec")
        time_1 = time.time()
        find_min()
        print(f"find_min: {time.time() - time_1} sec")
        time_1 = time.time()
        find_sum()
        print(f"find_sum: {time.time() - time_1} sec")
        time_1 = time.time()
        find_prod()
        print(f"find_prod: {time.time() - time_1} sec")
        time_1 = time.time()
        find_mean()
        print(f"find_prod: {time.time() - time_1} sec")
        self.assertTrue(True)

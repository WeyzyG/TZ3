import unittest, math, time
from statistics import mean
from myscript import find_max, find_min, find_sum, find_prod, find_mean, data


class SomeTest(unittest.TestCase):

    def test_max(self):
        self.assertEqual(find_max(), max(data))

    def test_min(self):
        self.assertEqual(find_min(), min(data))

    def test_sum(self):
        self.assertEqual(find_sum(), sum(data))

    def test_prod(self):
        self.assertEqual(find_prod(), math.prod(data))

    def test_mean(self):  # Дополнительный тест
        self.assertEqual(find_mean(), mean(data))

    def test_time(self):  # Тест на время
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


if __name__ == '__main__':
    unittest.main()

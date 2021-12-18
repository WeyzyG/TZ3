import unittest, math
from statistics import mean
from myscript import find_mean, data


class SomeTest(unittest.TestCase):

    def test_mean(self):  # Дополнительный тест
        self.assertEqual(find_mean(), mean(data))


if __name__ == '__main__':
    unittest.main()

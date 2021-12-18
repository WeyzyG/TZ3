import unittest
from myscript import find_sum, data


class SomeTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(find_sum(), sum(data))


if __name__ == '__main__':
    unittest.main()

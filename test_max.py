import unittest
from myscript import find_max, dat


class SomeTest(unittest.TestCase):

    def test_max(self):
        self.assertEqual(find_max(), max(data))


if __name__ == '__main__':
    unittest.main()

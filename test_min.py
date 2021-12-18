import unittest
from myscript import find_min, data


class SomeTest(unittest.TestCase):

    def test_min(self):
        self.assertEqual(find_min(), min(data))


if __name__ == '__main__':
    unittest.main()

import unittest, math
from myscript import find_prod, data


class SomeTest(unittest.TestCase):

    def test_prod(self):
        self.assertEqual(find_prod(), math.prod(data))


if __name__ == '__main__':
    unittest.main()

import unittest
from half_adder import half_adder


class HalfAdderFunctionTestCase(unittest.TestCase):

    def test_half_adder_different(self):
        self.assertEqual(half_adder(1, 0), (0, 1))
        self.assertEqual(half_adder(0, 1), (0, 1))

    def test_half_adder_equal(self):
        self.assertEqual(half_adder(1, 1), (1, 0))
        self.assertEqual(half_adder(0, 0), (0, 0))


if __name__ == '__main__':
    unittest.main()

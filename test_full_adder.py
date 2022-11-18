import unittest
from full_adder import full_adder


class FullAdderFunctionTestCase(unittest.TestCase):

    def test_full_adder_different(self):
        self.assertEqual(full_adder(0, 0, 1), (0, 1))
        self.assertEqual(full_adder(0, 1, 0), (0, 1))
        self.assertEqual(full_adder(0, 1, 1), (1, 0))
        self.assertEqual(full_adder(1, 0, 0), (0, 1))
        self.assertEqual(full_adder(1, 0, 1), (1, 0))
        self.assertEqual(full_adder(1, 1, 0), (1, 0))

    def test_full_adder_equal(self):
        self.assertEqual(full_adder(1, 1, 1), (1, 1))
        self.assertEqual(full_adder(0, 0, 0), (0, 0))


if __name__ == '__main__':
    unittest.main()

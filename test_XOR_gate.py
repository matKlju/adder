import unittest
from XOR_gate import XOR


class XORFunctionTestCase(unittest.TestCase):

    def test_XOR_different(self):
        self.assertEqual(XOR(1, 0), 1)
        self.assertEqual(XOR(0, 1), 1)

    def test_XOR_equal(self):
        self.assertEqual(XOR(1, 1), 0)
        self.assertEqual(XOR(0, 0), 0)


if __name__ == '__main__':
    unittest.main()

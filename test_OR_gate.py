import unittest
from OR_gate import OR


class ORFunctionTestCase(unittest.TestCase):

    def test_OR_different(self):
        self.assertEqual(OR(1, 0), 1)
        self.assertEqual(OR(0, 1), 1)

    def test_OR_equal(self):
        self.assertEqual(OR(1, 1), 1)
        self.assertEqual(OR(0, 0), 0)


if __name__ == '__main__':
    unittest.main()

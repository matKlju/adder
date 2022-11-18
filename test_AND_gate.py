import unittest
from AND_gate import AND


class ANDFunctionTestCase(unittest.TestCase):

    def test_AND_different(self):
        self.assertEqual(AND(1, 0), 0)
        self.assertEqual(AND(0, 1), 0)

    def test_AND_equal(self):
        self.assertEqual(AND(1, 1), 1)
        self.assertEqual(AND(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
    
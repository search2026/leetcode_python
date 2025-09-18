import unittest
from solutions.decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    def test_numDecodings(self):
        solution = Solution()
        s = "12"
        expect = 2
        actual = solution.method()
        self.assertEqual(expect, actual)

        s = "226"
        expect = 3
        actual = solution.method()
        self.assertEqual(expect, actual)

        s = "06"
        expect = 0
        actual = solution.method()
        self.assertEqual(expect, actual)

import unittest
from solutions.minimum_window_substring import Solution


class TestMinimumWindowSubstring(unittest.TestCase):
    def test_minWindow(self):
        solution = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        expect = "BANC"
        actual = solution.minWindow(s, t)
        self.assertEqual(expect, actual)

        s = "a"
        t = "a"
        expect = "a"
        actual = solution.minWindow(s, t)
        self.assertEqual(expect, actual)

        s = "a"
        t = "aa"
        expect = ""
        actual = solution.minWindow(s, t)
        self.assertEqual(expect, actual)

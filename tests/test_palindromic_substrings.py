import unittest

from solutions.palindromic_substrings import Solution


class TestPalindromicSubstrings(unittest.TestCase):
    def test_count_substrings(self):
        solution = Solution()
        s = "abc"
        expect = 3
        actual = solution.countSubstrings(s)
        self.assertEqual(expect, actual)

        s = "aaa"
        expect = 6
        actual = solution.countSubstrings(s)
        self.assertEqual(expect, actual)

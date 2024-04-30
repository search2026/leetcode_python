import unittest
from solutions.longest_palindromic_substring import Solution, Solution2


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_longest_palindromic_substring(self):
        solution = Solution()
        s = "babad"
        expected = "bab"
        self.assertEqual(solution.longest_palindrome(s), expected)

        s = "cbbd"
        expected = "bb"
        self.assertEqual(solution.longest_palindrome(s), expected)

    def test_longest_palindromic_substring2(self):
        solution = Solution2()
        s = "babad"
        expected = "aba"
        self.assertEqual(solution.longest_palindrome(s), expected)

        s = "cbbd"
        expected = "bb"
        self.assertEqual(solution.longest_palindrome(s), expected)

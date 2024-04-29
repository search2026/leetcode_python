import unittest
from solutions.valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        solution = Solution()
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(solution.isPalindrome(s))

        s = "race a car"
        self.assertFalse(solution.isPalindrome(s))

        s = " "
        self.assertTrue(solution.isPalindrome(s))

import unittest
from solutions.palindrome_number import Solution, Solution2


class TestPalindromeNumber(unittest.TestCase):
    def test_palindrome_number(self):
        solution = Solution()
        x = 121
        self.assertTrue(solution.isPalindrome(x))

        x = -121
        self.assertFalse(solution.isPalindrome(x))

        x = 10
        self.assertFalse(solution.isPalindrome(x))

    def test_palindrome_number2(self):
        solution = Solution2()
        x = 121
        self.assertTrue(solution.isPalindrome(x))

        x = -121
        self.assertFalse(solution.isPalindrome(x))

        x = 10
        self.assertFalse(solution.isPalindrome(x))

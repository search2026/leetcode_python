import unittest
from solutions.valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        solution = Solution()
        s = "()"
        self.assertTrue(solution.is_valid(s))

        s = "()[]{}"
        self.assertTrue(solution.is_valid(s))

        s = "(]"
        self.assertFalse(solution.is_valid(s))

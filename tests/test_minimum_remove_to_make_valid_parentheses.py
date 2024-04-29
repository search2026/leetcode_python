import unittest
from solutions.minimum_remove_to_make_valid_parentheses import Solution


class TestMinimumRemoveToMakeValidParentheses(unittest.TestCase):
    def test_minimum_remove_to_make_valid_parentheses(self):
        s = "lee(t(c)o)de)"
        expect = "lee(t(c)o)de"
        actual = Solution().min_remove_to_make_valid(s)
        self.assertEqual(expect, actual)

        s = "a)b(c)d"
        expect = "ab(c)d"
        actual = Solution().min_remove_to_make_valid(s)
        self.assertEqual(expect, actual)

        s = "))(("
        expect = ""
        actual = Solution().min_remove_to_make_valid(s)
        self.assertEqual(expect, actual)

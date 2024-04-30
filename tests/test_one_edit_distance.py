import unittest
from solutions.one_edit_distance import Solution


class TestOneEditDistance(unittest.TestCase):
    def test_one_edit_distance(self):
        solution = Solution()
        self.assertTrue(solution.isOneEditDistance("ab", "acb"))
        self.assertFalse(solution.isOneEditDistance("cab", "ad"))
        self.assertFalse(solution.isOneEditDistance("1202", "1213"))
        self.assertTrue(solution.isOneEditDistance("1203", "1213"))

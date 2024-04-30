import unittest
from solutions.valid_number import Solution


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        s = "0"
        self.assertTrue(solution.is_number(s))

        s = "e"
        self.assertFalse(solution.is_number(s))

        s = "."
        self.assertFalse(solution.is_number(s))
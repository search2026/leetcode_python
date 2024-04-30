import unittest
from solutions.reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):
    def test_reverse_integer(self):
        solution = Solution()
        x = 123
        self.assertEqual(solution.reverse(x), 321)

        x = -123
        self.assertEqual(solution.reverse(x), -321)

        x = 120
        self.assertEqual(solution.reverse(x), 21)

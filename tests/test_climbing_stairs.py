import unittest
from solutions.climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def test_climbing_stairs(self):
        solution = Solution()
        n = 2
        self.assertEqual(2, solution.climb_stairs(n))

        n = 3
        self.assertEqual(3, solution.climb_stairs(n))

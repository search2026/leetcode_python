import unittest
from solutions.min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def test_min_cost_climbing_stairs(self):
        solution = Solution()
        cost = [10, 15, 20]
        self.assertEqual(solution.minCostClimbingStairs(cost), 15)

        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(solution.minCostClimbingStairs(cost), 6)

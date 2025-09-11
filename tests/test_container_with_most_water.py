import unittest
from solutions.container_with_most_water import Solution


class TestContainerWithMostWater(unittest.TestCase):
    def test_max_area(self):
        solution = Solution()
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expect = 49
        actual = solution.maxArea(height)
        assert actual == expect

        height = [1, 1]
        expect = 1
        actual = solution.maxArea(height)
        assert actual == expect

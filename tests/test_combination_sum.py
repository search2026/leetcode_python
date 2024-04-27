import unittest
from solutions.combination_sum import Solution, Solution2


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        solution = Solution()
        candidates = [2, 3, 6, 7]
        target = 7
        expect = [[2, 2, 3], [7]]
        actual = solution.combination_sum(candidates, target)
        self.assertCountEqual(expect, actual)

        candidates = [2, 3, 5]
        target = 8
        expect = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        actual = solution.combination_sum(candidates, target)
        self.assertCountEqual(expect, actual)

        candidates = [2]
        target = 1
        expect = []
        actual = solution.combination_sum(candidates, target)
        self.assertCountEqual(expect, actual)

    def test_combination_sum2(self):
        solution = Solution2()
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expect = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        actual = solution.combination_sum(candidates, target)
        self.assertCountEqual(expect, actual)

        candidates = [2, 5, 2, 1, 2]
        target = 5
        expect = [[1, 2, 2], [5]]
        actual = solution.combination_sum(candidates, target)
        self.assertCountEqual(expect, actual)

import unittest
from solutions.combination_sum import Solution, Solution2, Solution3, Solution4


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

    def test_combination_sum3(self):
        solution = Solution3()
        k, n = 3, 7
        expect = [[1, 2, 4]]
        actual = solution.combination_sum3(k, n)
        self.assertCountEqual(expect, actual)

        k, n = 3, 9
        expect = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        actual = solution.combination_sum3(k, n)
        self.assertCountEqual(expect, actual)

        k, n = 4, 1
        expect = []
        actual = solution.combination_sum3(k, n)
        self.assertCountEqual(expect, actual)

    def test_combination_sum4(self):
        solution = Solution4()
        nums = [1, 2, 3]
        target = 4
        expect = 7
        actual = solution.combination_sum4(nums, target)
        self.assertEqual(expect, actual)

        nums = [9]
        target = 3
        expect = 0
        actual = solution.combination_sum4(nums, target)
        self.assertEqual(expect, actual)

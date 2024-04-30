import unittest
from solutions.permutations import Solution, Solution2


class TestPermutations(unittest.TestCase):
    def test_permutations(self):
        solution = Solution()
        nums = [1, 2, 3]
        expect = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        actual = solution.permute(nums)
        self.assertCountEqual(expect, actual)

        nums = [0, 1]
        expect = [[0, 1], [1, 0]]
        actual = solution.permute(nums)
        self.assertCountEqual(expect, actual)

        nums = [1]
        expect = [[1]]
        actual = solution.permute(nums)
        self.assertCountEqual(expect, actual)

    def test_permutations2(self):
        solution = Solution2()
        nums = [1, 1, 2]
        expect = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        actual = solution.permute_unique(nums)
        self.assertCountEqual(expect, actual)

        nums = [1, 2, 3]
        expect = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        actual = solution.permute_unique(nums)
        assert expect == actual
        self.assertCountEqual(expect, actual)

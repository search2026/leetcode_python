import unittest
from solutions.subsets import Solution, Solution2


class TestSubsets(unittest.TestCase):
    def test_subsets(self):
        solution = Solution()
        nums = [1, 2, 3]
        expect = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        actual = solution.subsets(nums)
        self.assertCountEqual(expect, actual)

        nums = [0]
        expect = [[], [0]]
        actual = solution.subsets(nums)
        self.assertCountEqual(expect, actual)

    def test_subsets2(self):
        solution = Solution2()
        nums = [1,2,2]
        expect = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        actual = solution.subsets_with_dup(nums)
        self.assertCountEqual(expect, actual)

        nums = [0]
        expect = [[], [0]]
        actual = solution.subsets_with_dup(nums)
        self.assertCountEqual(expect, actual)

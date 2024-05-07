import unittest
from solutions.find_minimum_in_rotated_sorted_array import Solution, Solution2


class TestMinimumInRotatedSortedArray(unittest.TestCase):
    def test_find_minimum_in_rotated_sorted_array(self):
        solution = Solution()
        nums = [3, 4, 5, 1, 2]
        expect = 1
        self.assertEqual(solution.find_min(nums), expect)

        nums = [4, 5, 6, 7, 0, 1, 2]
        expect = 0
        self.assertEqual(solution.find_min(nums), expect)

        nums = [11, 13, 15, 17]
        expect = 11
        self.assertEqual(solution.find_min(nums), expect)

    def test_find_minimum_in_rotated_sorted_array2(self):
        solution = Solution2()
        nums = [1, 3, 5]
        expect = 1
        self.assertEqual(solution.find_min(nums), expect)

        nums = [2, 2, 2, 0, 1]
        expect = 0
        self.assertEqual(solution.find_min(nums), expect)

import unittest
from solutions.search_in_rotated_sorted_array import Solution, Solution2


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_search_in_rotated_sorted_array(self):
        solution = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(solution.search(nums, target), 4)

        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(solution.search(nums, target), -1)

        nums = [1]
        target = 0
        self.assertEqual(solution.search(nums, target), -1)

    def test_search_in_rotated_sorted_array2(self):
        solution = Solution()
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 0
        self.assertEqual(solution.search(nums, target), 3)

        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 3
        self.assertEqual(solution.search(nums, target), -1)

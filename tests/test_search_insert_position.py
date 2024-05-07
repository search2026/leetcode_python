import unittest
from solutions.search_insert_position import Solution


class TestSearchInsertPosition(unittest.TestCase):
    def test_search_insert_position(self):
        solution = Solution()
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(solution.search_insert(nums, target), 2)

        nums = [1, 3, 5, 6]
        target = 2
        self.assertEqual(solution.search_insert(nums, target), 1)

        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(solution.search_insert(nums, target), 4)

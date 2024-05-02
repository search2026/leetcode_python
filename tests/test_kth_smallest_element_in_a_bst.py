import unittest
from solutions.kth_smallest_element_in_a_bst import Solution
from utils.TreeNode import deserialize


class TestKKthSmallestElementInABST(unittest.TestCase):
    def test_kth_smallest_element_in_a_bst(self):
        solution = Solution()
        root = deserialize("[3,1,4,null,2]")
        k = 1
        expect = 1
        actual = solution.kth_smallest(root, k)
        self.assertEqual(expect, actual)

        root = deserialize("[5,3,6,2,4,null,null,1]")
        k = 3
        expect = 3
        actual = solution.kth_smallest(root, k)
        self.assertEqual(expect, actual)

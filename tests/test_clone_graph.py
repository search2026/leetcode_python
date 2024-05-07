import unittest
from solutions.clone_graph import Solution


class TestCloneGraph(unittest.TestCase):
    def test_clone_graph(self):
        solution = Solution()
        adjust_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
        # actual = solution.cloneGraph(adjust_list)
        # self.assertEqual(actual, expected)
        #
        # adjust_list = [[]]
        # expected = [[]]
        # actual = solution.cloneGraph(adjust_list)
        # self.assertEqual(actual, expected)
        #
        # adjust_list = []
        # expected = []
        # actual = solution.cloneGraph(adjust_list)
        # self.assertEqual(actual, expected)

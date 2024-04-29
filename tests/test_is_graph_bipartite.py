import unittest
from solutions.is_graph_bipartite import Solution


class TestIsGraphBipartite(unittest.TestCase):
    def test_twoSum(self):
        is_graph_bipartite = Solution()
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        expect = False
        actual = is_graph_bipartite.is_bipartite(graph)
        self.assertEqual(expect, actual)

        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        expect = True
        actual = is_graph_bipartite.is_bipartite(graph)
        self.assertEqual(expect, actual)

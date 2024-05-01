import unittest
from solutions.shortest_way_to_form_string import Solution


class TestShortestWayToFormString(unittest.TestCase):
    def test_shortest_way_to_form_string(self):
        solution = Solution()
        source = "abc"
        target = "abcbc"
        expect = 2
        actual = solution.shortest_way(source, target)
        self.assertEqual(expect, actual)

        source = "abc"
        target = "acdbc"
        expect = -1
        actual = solution.shortest_way(source, target)
        self.assertEqual(expect, actual)

        source = "xyz"
        target = "xzyxz"
        expect = 3
        actual = solution.shortest_way(source, target)
        self.assertEqual(expect, actual)

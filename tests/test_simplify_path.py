import unittest
from solutions.simplify_path import Solution


class TestSimplifyPath(unittest.TestCase):
    def test_simplify_path(self):
        solution = Solution()
        path = "/home/"
        self.assertEqual(solution.simplify_path(path), "/home")

        path = "/home//foo/"
        self.assertEqual(solution.simplify_path(path), "/home/foo")

        path = "/home/user/Documents/../Pictures"
        self.assertEqual(solution.simplify_path(path), "/home/user/Pictures")

        path = "/../"
        self.assertEqual(solution.simplify_path(path), "/")

        path = "/a/./b/../../c/"
        self.assertEqual(solution.simplify_path(path), "/c")

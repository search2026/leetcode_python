import unittest
from solutions.implement_strstr import Solution


class TestStrStr(unittest.TestCase):
    def test_strstr(self):
        solution = Solution()
        haystack = "sadbutsad"
        needle = "sad"
        self.assertEqual(solution.strStr(haystack, needle), 0)

        haystack = "leetcode"
        needle = "leeto"
        self.assertEqual(solution.strStr(haystack, needle), -1)

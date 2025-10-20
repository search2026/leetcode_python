import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.longest_common_subsequence import Solution, Solution2, Solution3


class TestBlank(unittest.TestCase):
    def test_longest_common_subsequence1(self):
        solution = Solution()
        text1 = "abcde"
        text2 = "ace"
        expect = 3
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

        text1 = "abc"
        text2 = "abc"
        expect = 3
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

        text1 = "abc"
        text2 = "def"
        expect = 0
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

    def test_longest_common_subsequence1(self):
        solution = Solution3()
        text1 = "abcde"
        text2 = "ace"
        expect = 3
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

        text1 = "abc"
        text2 = "abc"
        expect = 3
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

        text1 = "abc"
        text2 = "def"
        expect = 0
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

    def test_longest_common_subsequence1(self):
        solution = Solution3()
        text1 = "abcde"
        text2 = "ace"
        expect = 3
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

        text1 = "abc"
        text2 = "abc"
        expect = 3
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

        text1 = "abc"
        text2 = "def"
        expect = 0
        actual = solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(expect, actual)

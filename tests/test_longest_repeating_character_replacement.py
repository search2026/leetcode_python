import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.longest_repeating_character_replacement import Solution


class TestlongestRepeatingCharacterReplacement(unittest.TestCase):
    def test_character_replacement(self):
        solution = Solution()
        s = "ABAB"
        k = 2
        expect = 4
        actual = solution.characterReplacement(s, k)
        self.assertEqual(expect, actual)

        s = "AABABBA"
        k = 1
        expect = 4
        actual = solution.characterReplacement(s, k)
        self.assertEqual(expect, actual)

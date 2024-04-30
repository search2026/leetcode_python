import unittest
from solutions.longest_substring_without_repeating_characters import Solution


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_longest_substring_without_repeating_characters(self):
        solution = Solution()
        s = "abcabcbb"
        self.assertEqual(3, solution.length_of_longest_substring(s))

        s = "bbbbb"
        self.assertEqual(solution.length_of_longest_substring(s), 1)

        s = "pwwkew"
        self.assertEqual(solution.length_of_longest_substring(s), 3)

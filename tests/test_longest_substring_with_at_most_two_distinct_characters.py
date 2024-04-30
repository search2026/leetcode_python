import unittest
from solutions.longest_substring_with_at_most_two_distinct_characters import Solution


class TestLongestSubstringWithAtMostTwoDistinctCharacters(unittest.TestCase):
    def test_longest_substring_with_at_most_two_distinct_characters(self):
        solution = Solution()
        s = "eceba"
        self.assertEqual(solution.length_of_longest_substring_two_distinct(s), 3)

        s = "ccaabbb"
        self.assertEqual(solution.length_of_longest_substring_two_distinct(s), 5)

        s = "a"
        self.assertEqual(solution.length_of_longest_substring_two_distinct(s), 1)

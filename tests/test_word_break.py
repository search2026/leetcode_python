import unittest
from solutions.word_break import Solution, Solution2


class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        solution = Solution()
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(solution.word_break(s, word_dict))

        s = "applepenapple"
        word_dict = ["apple", "pen"]
        self.assertTrue(solution.word_break(s, word_dict))

        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(solution.word_break(s, word_dict))

    def test_word_break2(self):
        solution = Solution2()
        s = "catsanddog"
        word_dict = ["cat", "cats", "and", "sand", "dog"]
        expect = ["cats and dog", "cat sand dog"]
        actual = solution.word_break(s, word_dict)
        self.assertCountEqual(expect, actual)

        s = "pineapplepenapple"
        word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
        expect = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
        actual = solution.word_break(s, word_dict)
        self.assertCountEqual(expect, actual)

        s = "catsandog"
        word_dict = [["cats", "dog", "sand", "and", "cat"]]
        expect = []
        actual = solution.word_break(s, word_dict)
        self.assertCountEqual(expect, actual)

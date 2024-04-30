import unittest
from solutions.reverse_words import Solution, Solution2


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        solution = Solution()
        s = "the sky is blue"
        expect = "blue is sky the"
        actual = solution.reverse_words(s)
        self.assertEqual(actual, expect)

        s = "hello world"
        expect = "world hello"
        actual = solution.reverse_words(s)
        self.assertEqual(actual, expect)

        s = "a good   example"
        expect = "example good a"
        actual = solution.reverse_words(s)
        self.assertEqual(actual, expect)

    def test_reverse_words2(self):
        solution = Solution2()
        s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
        expect = ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]
        solution.reverse_words(s)
        self.assertEqual(s, expect)

        s = ["a"]
        expect = ["a"]
        solution.reverse_words(s)
        self.assertEqual(s, expect)

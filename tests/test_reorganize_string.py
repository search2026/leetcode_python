import unittest
from solutions.reorganize_string import Solution, Solution2


class TestTwoSum(unittest.TestCase):
    def test_reorganize_string(self):
        solution = Solution()
        s = "aab"
        expect = "aba"
        actual = solution.reorganize_string(s)
        assert expect == actual

        s = "aaab"
        expect = ""
        actual = solution.reorganize_string(s)
        assert expect == actual

    def test_reorganize_string2(self):
        solution = Solution2()
        s = "aab"
        expect = "aba"
        actual = solution.reorganize_string(s)
        assert expect == actual

        s = "aaab"
        expect = ""
        actual = solution.reorganize_string(s)
        assert expect == actual

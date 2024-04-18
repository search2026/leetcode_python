import unittest
from solutions.roman_to_integer import Solution


class TestTwoSum(unittest.TestCase):
    def test_romantointeger(self):
        solution = Solution()
        s = "III"
        expect = 3
        actual = solution.roman_to_int(s)
        assert actual == expect

        s = "LVIII"
        expect = 58
        actual = solution.roman_to_int(s)
        assert actual == expect

        s = "MCMXCIV"
        expect = 1994
        actual = solution.roman_to_int(s)
        assert actual == expect

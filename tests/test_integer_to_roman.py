import unittest
from solutions.integer_to_roman import Solution


class TestTwoSum(unittest.TestCase):
    def test_integertoroman(self):
        solution = Solution()
        num = 3
        expect = "III"
        actual = solution.int_to_roman(num)
        assert actual == expect

        num = 58
        expect = "LVIII"
        actual = solution.int_to_roman(num)
        assert actual == expect

        num = 1994
        expect = "MCMXCIV"
        actual = solution.int_to_roman(num)
        assert actual == expect

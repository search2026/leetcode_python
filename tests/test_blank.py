import unittest
from solutions.blank import Solution

solution = Solution()


class TestTwoSum(unittest.TestCase):
    def test_method1(self):
        expect = 0
        actual = solution.method()
        assert actual == expect

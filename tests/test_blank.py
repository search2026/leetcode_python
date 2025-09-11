import unittest
from solutions.blank import Solution


class TestBlank(unittest.TestCase):
    def test_method1(self):
        solution = Solution()
        expect = 0
        actual = solution.method()
        assert actual == expect

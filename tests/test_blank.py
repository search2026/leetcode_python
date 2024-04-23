import unittest
from solutions.blank import Solution

solution = Solution()


class TestTwoSum(unittest.TestCase):
    def test_method1(self):
        expect = 0
        actual = solution.method()
        assert actual == expect

        self.assertEqual( actual, expect)
        self.assertCountEqual([1,3,2], [3,1, 2])
        # self.assertCountEqual([1,3,2], [4,1, 2])
        # self.assertListEqual([1,3,2], [3,1, 2])

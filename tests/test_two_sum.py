import unittest
from solutions.two_sum import Solution, Solution2, TwoSum


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expect = [0, 1]
        actual = solution.two_sum(nums, target)
        assert actual == expect

        nums = [3, 2, 4]
        target = 6
        expect = [1, 2]
        actual = solution.two_sum(nums, target)
        assert actual == expect

        nums = [3, 3]
        target = 6
        expect = [0, 1]
        actual = solution.two_sum(nums, target)
        assert actual == expect

    def test_two_sum2(self):
        solution = Solution2()
        nums = [2, 7, 11, 15]
        target = 9
        expect = [1, 2]
        actual = solution.two_sum(nums, target)
        assert actual == expect

        nums = [2, 3, 4]
        target = 6
        expect = [1, 3]
        actual = solution.two_sum(nums, target)
        assert actual == expect

        nums = [-1, 0]
        target = -1
        expect = [1, 2]
        actual = solution.two_sum(nums, target)
        assert actual == expect

    def test_two_sum3(self):
        two_sum = TwoSum()
        two_sum.add(1)
        two_sum.add(3)
        two_sum.add(5)
        self.assertTrue(two_sum.find(4))
        self.assertFalse(two_sum.find(7))

        two_sum = TwoSum()
        two_sum.add(3)
        two_sum.add(1)
        two_sum.add(2)
        self.assertTrue(two_sum.find(3))
        self.assertFalse(two_sum.find(6))

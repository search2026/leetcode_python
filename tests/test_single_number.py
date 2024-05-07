import unittest
from solutions.single_number import Solution, Solution2, Solution3


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        solution = Solution()
        nums = [2, 2, 1]
        expect = 1
        self.assertEqual(solution.single_number(nums), expect)

        nums = [4, 1, 2, 1, 2]
        expect = 4
        self.assertEqual(solution.single_number(nums), expect)

        nums = [1]
        expect = 1
        self.assertEqual(solution.single_number(nums), expect)

    def test_single_number2(self):
        solution = Solution2()
        nums = [2, 2, 3, 2]
        expect = 3
        self.assertEqual(solution.single_number(nums), expect)

        nums = [0, 1, 0, 1, 0, 1, 99]
        expect = 99
        self.assertEqual(solution.single_number(nums), expect)

        nums = [4, 1, 2, 1, 2]
        expect = 4
        self.assertEqual(solution.single_number(nums), expect)

    def test_single_number3(self):
        solution = Solution3()
        nums = [1, 2, 1, 3, 2, 5]
        expect = [3, 5]
        self.assertCountEqual(solution.single_number(nums), expect)

        nums = [-1, 0]
        expect = [-1, 0]
        self.assertCountEqual(solution.single_number(nums), expect)

        nums = [0, 1]
        expect = [1, 0]
        self.assertCountEqual(solution.single_number(nums), expect)

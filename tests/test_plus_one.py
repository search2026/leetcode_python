import unittest
from solutions.plus_one import Solution, Solution2


class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        solution = Solution()
        digits = [1, 2, 3]
        expected = [1, 2, 4]
        self.assertEqual(solution.plus_one(digits), expected)

        digits = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]
        self.assertEqual(solution.plus_one(digits), expected)

        digits = [9]
        expected = [1, 0]
        self.assertEqual(solution.plus_one(digits), expected)

    def test_plus_one2(self):
        solution = Solution2()
        digits = [1, 2, 3]
        expected = [1, 2, 4]
        self.assertEqual(solution.plus_one(digits), expected)

        digits = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]
        self.assertEqual(solution.plus_one(digits), expected)

        digits = [9]
        expected = [1, 0]
        self.assertEqual(solution.plus_one(digits), expected)

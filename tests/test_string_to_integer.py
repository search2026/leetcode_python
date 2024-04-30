import unittest
from solutions.string_to_integer import Solution, Solution2


class TestStringToInteger(unittest.TestCase):
    def test_string_to_integer(self):
        solution = Solution()
        s = "78"
        self.assertEqual(solution.a_to_i(s), 78)

        s = "   -78"
        self.assertEqual(solution.a_to_i(s), -78)

        s = "4193 with words"
        self.assertEqual(solution.a_to_i(s), 4193)

    def test_string_to_integer2(self):
        solution = Solution2()
        s = "78"
        self.assertEqual(solution.a_to_i(s), 78)

        s = "   -78"
        self.assertEqual(solution.a_to_i(s), -78)

        s = "4193 with words"
        self.assertEqual(solution.a_to_i(s), 4193)

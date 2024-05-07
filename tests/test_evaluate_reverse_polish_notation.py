import unittest
from solutions.evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def test_evaluate_reverse_polish_notation(self):
        solution = Solution()
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(solution.evalRPN(tokens), 9)

        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(solution.evalRPN(tokens), 6)

        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(solution.evalRPN(tokens), 22)

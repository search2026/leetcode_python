import unittest
from solutions.basic_calculator import Solution, Solution2, Solution3, Solution4


class TestBasicCalculator(unittest.TestCase):
    def test_basic_calculator(self):
        solution = Solution()
        s = "1 + 1"
        expect = 2
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

        s = " 2-1 + 2 "
        expect = 3
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

        s = "(1+(4+5+2)-3)+(6+8)"
        expect = 23
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

    def test_basic_calculator2(self):
        solution = Solution2()
        s = "3+2*2"
        expect = 7
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

        s = " 3/2 "
        expect = 1
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

        s = "3+5 / 2"
        expect = 5
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

    def test_basic_calculator3(self):
        solution = Solution3()
        s = "1 + 1"
        expect = 2
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

        s = " 6 - 4/2 "
        expect = 4
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

        s = "2*(5+5*2)/3+(6/2+8)"
        expect = 21
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

        s = "(2+6* 3+5- (3*14/7+2)*5)+3"
        expect = -12
        actual = solution.calculate(s)
        self.assertEqual(expect, actual)

    def test_basic_calculator4(self):
        solution = Solution4()
        expression = "e + 8 - a + 5"
        evalvars = ["e"]
        evalints = [1]
        expect = ["-1*a", "14"]
        actual = solution.basic_calculator_iv(expression, evalvars, evalints)
        self.assertCountEqual(expect, actual)

        expression = "e - 8 + temperature - pressure"
        evalvars = ["e", "temperature"]
        evalints = [1, 12]
        expect = ["-1*pressure", "5"]
        actual = solution.basic_calculator_iv(expression, evalvars, evalints)
        self.assertCountEqual(expect, actual)

        expression = "(e + 8) * (e - 8)"
        evalvars = []
        evalints = []
        expect = ["1*e*e", "-64"]
        actual = solution.basic_calculator_iv(expression, evalvars, evalints)
        self.assertCountEqual(expect, actual)

        expression = "(e + 8) * (e - 8)"
        evalvars = []
        evalints = []
        expect = ["1*e*e", "-64"]
        actual = solution.basic_calculator_iv(expression, evalvars, evalints)
        self.assertCountEqual(expect, actual)

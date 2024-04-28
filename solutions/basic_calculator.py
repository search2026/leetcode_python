# -*- coding: utf-8 -*-
import math
import re
from collections import defaultdict
from typing import List, Optional, Mapping
from functools import cmp_to_key


################################################
#
# Leetcode 224. Basic Calculator
# URL: https://leetcode.com/problems/basic-calculator/description/
# Difficulty: Hard
#
################################################


class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(i):
            res, digit, sign = 0, 0, 1

            while i < len(s):
                if s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                elif s[i] in '+-':
                    res += digit * sign
                    digit = 0
                    sign = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    subres, i = evaluate(i + 1)
                    res += sign * subres
                elif s[i] == ')':
                    res += digit * sign
                    return res, i
                i += 1

            return res + digit * sign

        return evaluate(0)


################################################
#
# Leetcode 227. Basic Calculator II
# URL: https://leetcode.com/problems/basic-calculator-ii/description/
# Difficulty: Medium
#
################################################


class Solution2:
    def calculate(self, s: str) -> int:
        num, pre_sign, stack = 0, '+', []
        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                elif pre_sign == '/':
                    stack.append(math.trunc(stack.pop() / num))
                pre_sign = c
                num = 0
        return sum(stack)


################################################
#
# Leetcode 770. Basic Calculator III
# URL: https://leetcode.com/problems/basic-calculator-iii/description/
# Difficulty: Hard
#
################################################


class Solution3:
    def calculate(self, s: str) -> int:
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                        (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        match op:
            case "+":
                operands.append(left + right)
            case "-":
                operands.append(left - right)
            case "*":
                operands.append(left * right)
            case "/":
                operands.append(int(left / right))


################################################
#
# Leetcode 770. Basic Calculator IV
# URL: https://leetcode.com/problems/basic-calculator-iv/description/
# Difficulty: Hard
#
################################################


class Atom:
    def __init__(self, h={}):
        self.h = defaultdict(int)
        for k, v in h.items(): self.h[k] += v

    def __add__(self, other):
        h = defaultdict(int)
        for k in self.h: h[k] += self.h[k]
        for k in other.h: h[k] += other.h[k]
        return Atom({k: v for k, v in h.items() if v})

    def __sub__(self, other):
        h = defaultdict(int)
        for k in self.h: h[k] += self.h[k]
        for k in other.h: h[k] -= other.h[k]
        return Atom({k: v for k, v in h.items() if v})

    def __mul__(self, other):
        def f(k1, k2):
            k1, k2 = k1.split('*'), k2.split('*')
            k = [x for x in k1 if x] + [x for x in k2 if x]
            return '*'.join(sorted(k)) if k else ''

        h = defaultdict(int)
        for k in self.h:
            for kk in other.h:
                h[f(k, kk)] += self.h[k] * other.h[kk]
        print('here', h, list(self.h.keys()), list(other.h.keys()))
        return Atom({k: v for k, v in h.items() if v})

    def __repr__(self):
        return str(self.h)

    def fmt(self):
        res = []
        for k, v in sorted(self.h.items(), key=lambda x: (-len(x[0].split('*')), x[0])):
            if k: res.append(f'{v}*{k}')
        if self.h['']: res.append(str(self.h['']))
        return res


class Parser:
    def __init__(self, s, h):
        self.tokens = deque(re.findall('[a-z]+|[0-9]+|\+|\*|-|\(|\)', s))
        self.h = h
        print(s)

    def _test(self, pred=lambda x: True):
        return self.tokens and pred(self.tokens[0])

    def _consume(self, pred=None):
        if pred: assert self._test(pred)
        return self.tokens.popleft()

    def _atom(self):
        if self._test(lambda x: x.isdigit()):
            return Atom({'': int(self._consume())})
        if self._test(lambda x: x.isalpha()):
            x = self._consume()
            if x in self.h:
                return Atom({'': self.h[x]})
            return Atom({x: 1})
        if self._test(lambda x: x == '('):
            self._consume()
            res = self._l2()
            self._consume()
            return res

    def _l1(self):
        ops = {
            '*': lambda x, y: x * y,
        }
        res = self._atom()
        while self._test(lambda x: x in ops):
            op = ops[self._consume()]
            res = op(res, self._atom())
        return res

    def _l2(self):
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
        }
        res = self._l1()
        while self._test(lambda x: x in ops):
            op = ops[self._consume()]
            res = op(res, self._l1())
        return res

    def parse(self):
        res = self._l2()
        return res.fmt()


class Solution4:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        return Parser(expression, dict(zip(evalvars, evalints))).parse()

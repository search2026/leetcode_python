import unittest
from solutions.min_stack import MinStack


class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)  # return -3
        min_stack.pop()
        min_stack.top()  # return 0
        self.assertEqual(min_stack.getMin(), -2)  # return -2

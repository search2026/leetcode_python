import unittest
from solutions.count_and_say import Solution


class TestCountAndSay(unittest.TestCase):
    def test_count_and_say(self):
        solution = Solution()
        n = 1
        self.assertEqual("1", solution.count_and_say(n))

        n = 4
        self.assertEqual("1211", solution.count_and_say(n))

        n = 5
        self.assertEqual("111221", solution.count_and_say(n))

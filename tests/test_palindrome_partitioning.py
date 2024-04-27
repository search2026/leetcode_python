import unittest
from solutions.palindrome_partitioning import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def test_palindrome_partitioning(self):
        solution = Solution()
        s = "aab"
        expect = [["a", "a", "b"], ["aa", "b"]]
        actual = Solution().partition(s)
        self.assertCountEqual(expect, actual)

        s = "a"
        expect = [["a"]]
        actual = Solution().partition(s)
        self.assertCountEqual(expect, actual)

import unittest
from solutions.group_anagrams import Solution, Solution2


class TestReverseWords(unittest.TestCase):
    def test_group_anagrams(self):
        solution = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expect = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual = solution.groupAnagrams(strs)
        self.assertEqual(actual, expect)

        strs = [""]
        expect = [[""]]
        actual = solution.groupAnagrams(strs)
        self.assertEqual(actual, expect)

        strs = ["a"]
        expect = [["a"]]
        actual = solution.groupAnagrams(strs)
        self.assertEqual(actual, expect)

    def test_group_anagrams2(self):
        solution = Solution2()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expect = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual = solution.groupAnagrams(strs)
        self.assertEqual(actual, expect)

        strs = [""]
        expect = [[""]]
        actual = solution.groupAnagrams(strs)
        self.assertEqual(actual, expect)

        strs = ["a"]
        expect = [["a"]]
        actual = solution.groupAnagrams(strs)
        self.assertEqual(actual, expect)

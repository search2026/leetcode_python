import unittest


from solutions.valid_anagram import Solution, Solution2, Solution3


class TestValidAnagram(unittest.TestCase):
    def test_is_anagram(self):
        solution = Solution()
        s = "anagram"
        t = "nagaram"
        self.assertTrue(solution.isAnagram(s, t))

        s = "rat"
        t = "car"
        self.assertFalse(solution.isAnagram(s, t))

    def test_is_anagram2(self):
        solution = Solution2()
        s = "anagram"
        t = "nagaram"
        self.assertTrue(solution.isAnagram(s, t))

        s = "rat"
        t = "car"
        self.assertFalse(solution.isAnagram(s, t))

    def test_is_anagram3(self):
        solution = Solution3()
        s = "anagram"
        t = "nagaram"
        self.assertTrue(solution.isAnagram(s, t))

        s = "rat"
        t = "car"
        self.assertFalse(solution.isAnagram(s, t))

import unittest
from solutions.text_justification import Solution


class TestTextJustification(unittest.TestCase):
    def test_text_justification(self):
        solution = Solution()
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        max_width = 16
        expect = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        actual = solution.full_justify(words, max_width)
        self.assertEqual(expect, actual)

        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        max_width = 16
        expect = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        actual = solution.full_justify(words, max_width)
        self.assertEqual(expect, actual)

        words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
                 "Art", "is", "everything", "else", "we", "do"]
        max_width = 20
        expect = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        actual = solution.full_justify(words, max_width)
        self.assertEqual(expect, actual)

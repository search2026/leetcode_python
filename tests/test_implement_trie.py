import unittest
from solutions.implement_trie import Trie


class TestImplementTrie(unittest.TestCase):
    def test_implement_trie(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))  # return True
        self.assertFalse(trie.search("app"))  # return False
        self.assertTrue(trie.startsWith("app"))  # return True
        trie.insert("app")
        self.assertTrue(trie.search("app"))  # return True

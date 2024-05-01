# -*- coding: utf-8 -*-


################################################
#
# Leetcode 208. Implement Trie (Prefix Tree)
# URL: https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Difficulty: Medium
#
################################################

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]

        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True

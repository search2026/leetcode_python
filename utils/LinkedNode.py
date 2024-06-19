# -*- coding: utf-8 -*-

class LinkedNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

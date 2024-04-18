# -*- coding: utf-8 -*-

import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def stringToListNode(cls, string):
        # Generate list from the input
        numbers = json.loads(string)

        # Now convert that list into linked list
        dummy_root = ListNode(0)
        p = dummy_root
        for number in numbers:
            p.next = ListNode(number)
            p = p.next

        return p.next

    @classmethod
    def listNodeToString(cls, node) -> str:
        if not node:
            return "[]"

        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"

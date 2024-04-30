# -*- coding: utf-8 -*-

import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
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

    @classmethod
    def arrayToListNode(cls, arr):
        dummy_root = ListNode(0)
        p = dummy_root
        if len(arr) == 0:
            return None

        for i in range(0, len(arr)):
            p.next = ListNode(arr[i])
            p = p.next

        return dummy_root.next

    @classmethod
    def listNodeToArray(cls, node):  # convert linked list to array
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr

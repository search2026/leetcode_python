# -*- coding: utf-8 -*-
from typing import Optional
from utils.ListNode import ListNode


################################################
#
# Leetcode 2. Add Two Numbers
# URL: https://leetcode.com/problems/add-two-numbers/description/
# Difficulty: Medium
#
################################################

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        p = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum_two_digits = digit1 + digit2 + carry
            digit = sum_two_digits % 10
            carry = sum_two_digits // 10

            p.next = ListNode(digit)
            p = p.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        res = dummy_head.next
        # dummy_head.next = None
        return res

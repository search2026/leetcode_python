# -*- coding: utf-8 -*-
import heapq
from typing import Optional, List
from utils.ListNode import ListNode


################################################
#
# Leetcode 23. Merge k Sorted Lists
# URL: https://leetcode.com/problems/merge-k-sorted-lists/description/
# Difficulty: Hard
#
################################################


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        if not lists:
            return None

        heap = []
        dummy = p = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(heap, (i.val, i))

        while heap:
            node = heapq.heappop(heap)[1]
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

        return dummy.next

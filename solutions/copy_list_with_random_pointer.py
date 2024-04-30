# -*- coding: utf-8 -*-
from typing import Optional
from utils.ListNode import ListNode


################################################
#
# Leetcode 138. Copy List with Random Pointer
# URL: https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Difficulty: Medium
#
################################################


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    @classmethod
    def arrayToListNode(cls, arr):
        if len(arr) == 0:
            return None

        dummy_root = p = Node(0)

        for i in range(0, len(arr)):
            p.next = Node(arr[i][0], arr[i][1])
            p = p.next

        return dummy_root.next

    @classmethod
    def listNodeToArray(cls, node):
        arr = []
        while node:
            new_arr = [node.val, node.random.val if node.random else None]
            arr.append(new_arr)
            node = node.next
        return arr


class Solution:
    def copy_random_list(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val,None,None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]




    # def copy_random_list(self, head: ‘Node’) -> ‘Node’:
    #     if head is None:
    #         return None
    #
    #     # 创建一个字典来存储原链表节点和复制节点的映射关系
    #     mapping = {}
    #
    #     # 第一次遍历原链表，创建复制节点，并将原节点和复制节点的映射关系存储到字典中
    #     cur = head
    #     while cur:
    #         mapping[cur] = Node(cur.val, None, None)
    #         cur = cur.next
    #
    #     # 第二次遍历原链表，根据映射关系设置复制节点的next和random指针
    #     cur = head
    #     while cur:
    #         if cur.next:
    #             mapping[cur].next = mapping[cur.next]
    #         if cur.random:
    #             mapping[cur].random = mapping[cur.random]
    #         cur = cur.next
    #
    #     # 返回复制链表的头节点
    #     return mapping[head]
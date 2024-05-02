# -*- coding: utf-8 -*-
import collections
import json


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

    @classmethod
    def stringToTreeNode(cls, in_str):
        in_str = in_str.strip()
        in_str = in_str[1:-1]
        if not in_str:
            return None

        input_values = [s.strip() for s in in_str.split(",")]
        root = TreeNode(int(input_values[0]))
        node_queue = [root]
        front = 0
        index = 1
        while index < len(input_values):
            node = node_queue[front]
            front = front + 1

            item = input_values[index]
            index = index + 1
            if item != "null":
                left_number = int(item)
                node.left = TreeNode(left_number)
                node_queue.append(node.left)

            if index >= len(input_values):
                break

            item = input_values[index]
            index = index + 1
            if item != "null":
                right_number = int(item)
                node.right = TreeNode(right_number)
                node_queue.append(node.right)
        return root

    @classmethod
    def treeToList(cls, root):
        # FIXME: bug exists
        if root is None:
            return [None]
        else:
            result = [root.val]
            if root.left is None and root.right is None:
                return result

            if root.left:
                result += cls.treeToList(root.left)
            else:
                result.append(None)

            if root.right:
                result += cls.treeToList(root.right)
            elif root.left.left or root.left.right:
                result.append(None)

            return result

    @classmethod
    def isSame(cls, me, that):
        if me is None and that is None:
            return TreeNode
        if (me is None and that is not None) or (me is not None and that is None):
            return False
        if me.val != that.val:
            return False
        if not cls.isSame(me.left, that.left):
            return False
        return cls.isSame(me.right, that.right)

    @classmethod
    def integerListToString(cls, nums, len_of_list=None):
        if not len_of_list:
            len_of_list = len(nums)
        return json.dumps(nums[:len_of_list])


def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def arrayToTreeNode(arr: list) -> TreeNode:
    if not arr:
        return None
    nodes = [None if not val else TreeNode(int(val))
             for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def serialize(root: TreeNode):
    # use level order traversal to match LeetCode's serialization format
    res = []
    queue = collections.deque([root])
    while queue:
        node = queue.pop()
        if node:
            res.append(str(node.val))
            queue.appendleft(node.left)
            queue.appendleft(node.right)
        else:
            # you can use any char to represent null
            # empty string means test for a non-null node is simply: flat_bt[i]
            res.append(None)
    return res

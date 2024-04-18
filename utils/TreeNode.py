# -*- coding: utf-8 -*-
import json


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

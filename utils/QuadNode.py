# -*- coding: utf-8 -*-


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, is_leaf, top_left, top_right, bottom_left, bottom_right):
        self.val = val
        self.isLeaf = is_leaf
        self.topLeft = top_left
        self.topRight = top_right
        self.bottomLeft = bottom_left
        self.bottomRight = bottom_right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        cur_level = [root]
        while cur_level:
            cur_level_val = []
            next_level = []
            for cur_node in cur_level:
                cur_level_val.append(cur_node.val)
                if cur_node.left: next_level.append(cur_node.left)
                if cur_node.right: next_level.append(cur_node.right)
            res.append(cur_level_val)
            cur_level = next_level
        return res




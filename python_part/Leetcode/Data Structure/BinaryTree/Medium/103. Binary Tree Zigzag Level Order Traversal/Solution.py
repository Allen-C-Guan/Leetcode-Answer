# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        cur_level = [root]
        res = []
        while cur_level:
            cur_level_val = []
            next_level = []
            for n in cur_level:
                cur_level_val.append(n.val)
                if n.left: next_level.append(n.left)
                if n.right: next_level.append(n.right)
            cur_level = next_level
            if len(res) % 2: cur_level_val.reverse()
            res.append(cur_level_val)
        return res

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
foo = Solution()
foo.zigzagLevelOrder(n1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if root is None:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        res = []
        helper(root)
        return res





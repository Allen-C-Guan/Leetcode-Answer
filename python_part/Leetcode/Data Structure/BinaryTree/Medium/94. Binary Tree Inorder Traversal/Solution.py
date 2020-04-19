# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inOrder(root)
        return self.res

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        self.res.append(root.val)
        self.inOrder(root.right)

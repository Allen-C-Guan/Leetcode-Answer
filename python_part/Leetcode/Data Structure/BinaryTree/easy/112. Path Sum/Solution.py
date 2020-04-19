# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:return False
        sum -= root.val
        if root.left is None and root.right is None: return sum == 0
        return self.hasPathSum(root.right,sum) or self.hasPathSum(root.left,sum)





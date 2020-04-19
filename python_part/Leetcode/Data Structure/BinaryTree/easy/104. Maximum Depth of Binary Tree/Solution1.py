# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



'''
最大深度问题是个递归问题，可以使用DFS的思想来解决问题：

递归公式：

    maxDepth(T) = 1+max(maxDepth(T.left), maxDepth(T.right))
    
根据以上递归公式，可以得到递归出口为：

    if T is None -->  return 0
    
    
'''

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1


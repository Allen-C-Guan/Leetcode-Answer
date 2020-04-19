# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



'''
题中没有说要求，但是要求是用pre-order来展开。所以我们就用preorder。
思路为：
1. 我们把right subtree 放在left subtree的最右下角的位置
2. 把left subtree 放在 right subtree的位置
3. left subtree 清零。

'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        if root.left is not None:
            if root.right is None:
                root.right = root.left
            else:
                cur = root.left
                while cur.right:
                    cur = cur.right
                cur.right = root.right
                root.right = root.left
            root.left = None
        self.flatten(root.right)








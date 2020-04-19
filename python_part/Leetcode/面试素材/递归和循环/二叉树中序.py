# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Recursive:
    def inorderTraversal(self,root):
        if root:
            self.inorderTraversal(root.left)
            res.append(root.val)
            self.inorderTraversal(root.right)
res = []




class iterate:
    def inorderTraversal(self, root):
        res = []
        if not root:
            return res
        stack = []
        cur = root
        while stack or cur:
            while cur:   # 先疯狂向左，从上道下入栈，一直到底
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()  # 出栈
            res.append(cur.val) # 访问
            cur = cur.right # 访问右边
        return res
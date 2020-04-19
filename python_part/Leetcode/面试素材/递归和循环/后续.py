class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) :
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :        # 先左
                stack.append(node.left)
            if node.right:        # 后右
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]



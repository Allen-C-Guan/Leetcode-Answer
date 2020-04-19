# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
我们就用验证array是不是sorted的方法来验证用inorder来遍历的tree就行了

只要记录前一个值，然后拿当前的和前一个比就行了

'''
class Solution:
    def __init__(self):
        self.pre_val = float("-inf")
        self.res = True

    def isValidBST(self, root: TreeNode) -> bool:
        self.helper(root)
        return self.res

    def helper(self, root: TreeNode):
        if root is None:
            return
        self.helper(root.left)

        if root.val <= self.pre_val:
            self.res = False
        self.pre_val = root.val

        self.helper(root.right)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n2.left = n1
n2.right = n3

foo = Solution()
print(foo.isValidBST(n2))




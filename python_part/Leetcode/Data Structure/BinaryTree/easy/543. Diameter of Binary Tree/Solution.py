# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.totol = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.buildMaxHeight(root)
        return self.totol
    '''
    思路还是和之前一样：
    1. 函数的功能是：找到当前最大深度。
    2. 判定当前左右子树最大深度的和与max做对比
    
    但是这里有个问题，就是最大值问题！！最大 意味着不需要记录任何中间过程，所有没必要记录中间过程
    
    '''
    def buildMaxHeight(self,root): # 找到当前位置最大height
        if root is None:
            return TreeNode(0)
        maxheight = TreeNode(None)

        maxheight.left = self.buildMaxHeight(root.left)
        maxheight.right = self.buildMaxHeight(root.right)

        maxheight.val = max(maxheight.left.val, maxheight.right.val)+1

        if maxheight.left.val + maxheight.right.val + 1 > self.totol:
            self.totol = maxheight.left.val + maxheight.right.val

        return maxheight

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)


n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5


foo = Solution()
print(foo.diameterOfBinaryTree(n1))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
这个思路是错的！！！
但是我们可以把这个思路重新变换一下：
变成只对一个root下的subtree的三代之间的关系而言，而不是整个tree。
因此 一个root的大小应该是；
 max(root.val + 孙子 , root.left + root.right) 

很遗憾这个递归很明显就是很多重复项，因此最后超时了，但是结果是对的。

重复怎么办？ DP解决问题啊。 只要记录孙子和父亲结果就可以节省了很多时间

'''
class Solution:
    def rob(self, root: TreeNode) -> int: # 递归的功能就是以root为根的subtree的能偷的最大值
        if root is None:
            return 0
        res = 0
        # 计算若包括当前节点的情况
        if root.left is not None:
            res += self.rob(root.left.left)+self.rob(root.left.right)
        if root.right is not None:
            res += self.rob(root.right.left)+self.rob(root.right.right)

        return max(res + root.val, self.rob(root.left)+self.rob(root.right))

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4

foo = Solution()
print(foo.rob(n1))
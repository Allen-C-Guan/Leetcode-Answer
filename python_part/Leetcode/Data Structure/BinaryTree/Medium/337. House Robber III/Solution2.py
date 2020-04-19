# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
怎么去记录这个中间过程啊？？
如果我们想用之前的办法， 通过记录father，grad——father的方法很明显根本不可以用递归实现！！！！！
因为左手倒右手的方法并不适合递归。递归是从上到下（从大到小）。但是左手倒右手的方法是从下往上，从小到大。
因此我们只能用dict 来记录所有中间过程！！！。
在进入递归的时候。首先就要要看看当前的点是否已经在dict里面了。如果是的话就不用继续往下算了


用dict来记录中间过程，并在递归开始的时候设置一个哨兵，检查是否已经计算过了。这个办法简直就是作弊！！！


'''
class Solution:
    def rob(self, root: TreeNode) -> int: # 递归的功能就是以root为根的subtree的能偷的最大值
        return self.helper(root, {})

    def helper(self,root: TreeNode, memo: dict):
        if root is None:
            return 0
        if root in memo:     # 这就是说！如果已经算过了，那就不用算了！！！！
            return memo[root]
        res = 0
        # 计算若包括当前节点的情况
        if root.left is not None:
            res += self.helper(root.left.left, memo)+self.helper(root.left.right,memo)
        if root.right is not None:
            res += self.helper(root.right.left, memo)+self.helper(root.right.right, memo)
        res = max(res + root.val, self.helper(root.left, memo)+self.helper(root.right, memo))
        memo[root] = res

        return res





n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4

foo = Solution()
print(foo.rob(n1))
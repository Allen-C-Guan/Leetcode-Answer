# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List

'''
我的思路是：
通过DFS，随便找一条从root到q的路径为path1，在随便找一条为path2。
若两者有共同祖先，那么，path1 和 path2 至少有一个共同点。
把所有共同点中最后的那个（最深的）拿出来就行了。


思路是正确的，但是超时了。
但我通过对path的维护，而不是copy，勉强没有超时，但是效率很低。
我又把list的查找从后向前以后， 速度有质的提升。
'''
class Solution:
    def __init__(self):
        self.flag = False   #为了打破递归而设置
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        self.helper(root,p,path1)
        self.flag = False
        path2 = []
        self.helper(root,q,path2)

        # 这里一定要倒着找相同！！不然太费时了 这相当于两个for循环。
        for i in range(len(path1)-1, -1, -1):  # 最后一个一定是none，到着算
            if path1[i] is not None and path1[i] in path2: return path1[i]

    def helper(self,root:TreeNode,target:TreeNode, path: List[TreeNode]):
        path.append(root)
        if root is None:
            return
        # path = path.copy()
        if root == target:
            self.flag = True
            return

        self.helper(root.left,target,path)
        if self.flag: return   # 每个递归出口都要做两件事情 1. 检查是否需要退出递归了。2. stack的维护
        path.pop()
        # 关于如何在递归中维护list。一般的结构是
        # 1.加入当前点
        # 2. 递归
        # 3. 递归下一行就pop
        # 这样，每次进入递归，都加入一个在list里面，每一次出来，就pop一个。进一个，出一个，当前list恢复原样

        self.helper(root.right,target,path)
        if self.flag: return
        path.pop()









# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n4.left = n6
# n5.left = n7
#
# m1 = TreeNode(1)
# m2 = TreeNode(2)
# m1.left = m2
#
# foo = Solution()
# foo.lowestCommonAncestor(m1,m1,m2)


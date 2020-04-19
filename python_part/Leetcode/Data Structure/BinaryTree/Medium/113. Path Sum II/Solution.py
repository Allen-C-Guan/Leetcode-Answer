# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
'''
本题思路主要就是回朔法。
因为问题本身是从head 到leaf，因此问题就很简单了。
一边做DFS一边记录path就行了。 对path进行回朔即可
'''
class Solution:
    def __init__(self):
        self.res = []
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return self.res
        self.helper(root,sum,[])
        return self.res
    def helper(self, root: TreeNode, sum: int, path:List[int]):
        sum -= root.val
        path = path.copy()
        path.append(root.val) #记录当前位置
        # 出口
        if root.left is None and root.right is None:  # 回朔点（叶子点），终点了
            if sum == 0:
                self.res.append(path)
            return
        # 未到出口
        if root.left is not None:
            self.helper(root.left,sum,path)   # 这里因为我们用了copy，所以在一个递归里面，如果你不去改变，那path是不会变的。即使递归入口之后也不会变。
                                            # 比如这里即使递归进入以后path就把left加进去了，但是一旦递归出来以后，path又变成了root结尾了。这就是因为copy的作用
        if root.right is not None:
            self.helper(root.right,sum,path)



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n3
n1.left = n2

foo = Solution()
print(foo.pathSum(n1,3))







# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
本题在用了level order的方法。
实现的方法在于：
1. 用一个list记录当前level的node，用另一list来记录下一个level的node。
2. while循环判定当前层是否还有node。如果没有了就不用继续了。

'''



from typing import List
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        cur_level = [root]
        while cur_level:  # while 循环在以list为flag的时候，会以list的空作为跳出条件，而如果cur_level均是None的时候，下一个cur——level就会是空，因为None不会有儿子了。
            cur_value = []
            next_level = []
            for cur in cur_level:
                if cur is not None:
                    cur_value.append(cur.val)
                    #方法1
                    if cur.left is not None:
                        next_level.append(cur.left)
                    if cur.right is not None:
                        next_level.append(cur.right)
                    # 方法2
                    # next_level.extend([cur.left, cur.right])  # extend是list的合并，append是list作为一个对象放在list中，形式上的区别在于是否保留括号
            if cur_value:  #list 在作为条件的时候，空为false！
                res.append(cur_value)
            cur_level = next_level
        res.reverse()  # reverse是inplace的做法，没有return
        return res


n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(13)
n1.left = n2
n1.right = n3
foo = Solution()

print(foo.levelOrderBottom(n1))



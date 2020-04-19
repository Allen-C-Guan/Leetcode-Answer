# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
'''
递归的本质就是堆栈！ 所有可以用递归写的，都可以用迭代+堆栈来完成，只不过是方不方便的事情

从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，先压右孩子再压左孩子。

在这个算法中，输出是stack的pop的结果，即push的反序，到最终结果的顺序按照 Top->Bottom 和 Left->Right，符合前序遍历的顺序。
'''


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            cur_node = stack.pop()
            res.append(cur_node.val)
            if cur_node.right: stack.append(cur_node.right)
            if cur_node.left: stack.append(cur_node.left)
        return res

n3 = TreeNode(3)
n2 = TreeNode(2)
n1 = TreeNode(1)
n3.left = n1
n3.right = n2
foo = Solution()
foo.preorderTraversal(n3)
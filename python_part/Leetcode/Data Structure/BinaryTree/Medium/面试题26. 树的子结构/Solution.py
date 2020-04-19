# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None: return False
        if self.helper(A, B):  # 如果A中包含B的全部，那就是找到了，不用继续找了
            self.res = True
        else:
            self.isSubStructure(A.left, B)  # 找找A.left 和 B
            self.isSubStructure(A.right, B)
        return self.res

    def helper(self, A: TreeNode, B: TreeNode) -> bool:  # 判定以A为root的节点是否包含全部B结构
        if B is None:
            return True
        if A is None:
            return False
        if A.val == B.val:
            return self.helper(A.left, B.left) and self.helper(A.right, B.right)
        else:
            return False

A = TreeNode(3)
B = TreeNode(3)
foo = Solution()
foo.isSubStructure(A, B)
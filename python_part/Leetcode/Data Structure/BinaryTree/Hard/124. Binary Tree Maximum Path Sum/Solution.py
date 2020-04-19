# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.half_dict = {None:0}
        self.res = float("-inf")

    def buildHelpDict(self, root) -> int: #  实现以root为head的单边最大值(一定要包括root，可以不包括child(光秃一个root是可以的） root是一定包括的）
        if root is None:
            return 0
        if root in self.half_dict:
            return self.half_dict[root]
        left = max(0, self.buildHelpDict(root.left)) # 0说明不要left了
        right = max(0, self.buildHelpDict(root.right)) # 同理 0说明不要right了
        mid = max(left, right) + root.val
        self.half_dict[root] = mid
        self.res = max(self.res, left + right + root.val)  # 以root为head的最大路径等于 left+right+ head
        return mid

    def maxPathSum(self, root: TreeNode) -> int:
        self.buildHelpDict(root)
        return int(self.res)



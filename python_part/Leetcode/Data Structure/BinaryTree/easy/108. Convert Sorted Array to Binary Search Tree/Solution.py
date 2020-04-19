# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
'''
只要是BST（binary search tree) 就一定要记得in order去遍历BST得到的一定是 sorted array。
但可惜这个思路不行。。。
可以用二分法来建立node

'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode: # 递归功能是建立当前节点，并将其左右子树分好区域
        if not nums:
            return
        mid = int(len(nums)/2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


'''
这里就充分应用了list作为条件的时候的作用： list作为条件的时候，list为空表示false。list非空就是True。
'''
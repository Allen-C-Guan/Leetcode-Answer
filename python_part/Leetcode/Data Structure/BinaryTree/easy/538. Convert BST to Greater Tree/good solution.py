'''
这是一个BST啊 用性质啊！！ in order 得到的就是sorted array啊

这道题是要求比他大，那么我们就反用in order来累加就行了。
但是由于是递归，累加需要 全局变量，就用一个类变量就行了。
在一个类里，类变量就是类中的全局变量。递归变换的只是local变量。在函数内部的变量

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is not None:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)
        return root

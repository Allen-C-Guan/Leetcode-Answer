# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
我们要充分利用二叉树的规律！！！
二叉树对于递归而言有及其优秀的特性。
1. 二叉树具有链表的特性，及揪着头就可以带动整个subtree，这给二叉树的变换提供了很多的便利。
2. 同样是二叉树链表的特性。由于有next的属性。不需要记录当前位置和index。只要关心递归关心就行。不用劳心更改index，堆栈维护等繁琐的问题。
    由于二叉树只有next。因此我们通常都是建立和children的关系，而不是和father的关系！如果每个点都照顾好自己的children，那么结构就固定下来了。
3. 二叉树是需要return node的来保证父子关系的传递的。

'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

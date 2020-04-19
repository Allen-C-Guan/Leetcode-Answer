# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
这题的思路：
中心思想在于。以某点为根的最长长度等于左右子树的高度之和

思路依旧是：
1. 递归的功能为：找到当前根下的最大高度
2. 那么当前最大长度等于左右子树的最大高度的和
3. 返回最大高度 left + right + 1 

对DFS的讨论：

不管是inorder preorder 在或者是 postorder 本质上都是一种 DFS。
而DFS 是一种自下而上的递归。因此递归出口一定在Tree的底端！
因此递归关系自然也是自下而上而上的递归。
因此处理数据通常发生在递归之后。即数据的处理通常写在递归之后。
这也就是说，递归是在归的时候进行计算的！

而递归的入口之后的代码，都可以把递归入口所得到的数据当成已知了。




'''
class Solution:
    def __init__(self):
        self.totol = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.totol

    def helper(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.max = max(self.max, left+right)  #此时right和left的高度一定都是已知的。
        return max(left, right) + 1  # 反向递归计算

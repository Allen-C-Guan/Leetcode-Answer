# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
这里要注意：什么才是叶子节点？
1. 指的是没有left和right才叫叶子节点。 因此递归终点必然就是left和right都是None。
2. 于此同时，如果以None为return，return的高度应该是0，可是以不是None结尾，return的必然是1。
3. 递归分支：在递归的过程中无非会遇到3类
    1. left right双全 ： 那么就取小的值
    2. left和right只有一个： 这类不是叶子，就一定要遍历下去。但是又不能取左右最小值。所以只把存在的那个分支进行下去就行了
    3. left right全无： 叶子节点。递归结束。返回

'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        return self.helper(root)

    def helper(self,root):
        if root.left is None and root.right is None: return 1
        if root.left is None: return self.helper(root.right) + 1
        if root.right is None: return self.helper(root.left) + 1
        return min(self.helper(root.right),self.helper(root.left))+1
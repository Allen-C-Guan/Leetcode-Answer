class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
新的思路为
最近祖先必有性质： root的左子树，右子树以及自己中，包含两个目标。

因为若非最近祖先， 一定会有两个目标值在左右一个子树中间，而不是两个。
因此用true 和false来代表 所被找的内容是否在当前root下。然后用left和right是不是true来判定当前root是不是他们的祖先。

这里由于递归的特性，无法终止递归。因此我们采用的方法是，设置个全局遍历。然后等遍历自然结束。在返回
'''
class Solution:
    def __init__(self):
        self.flag = None  #为了打破递归而设置
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root:TreeNode):
            if not root:
                return False
            mid = root == p or root == q
            left = helper(root.left)
            right = helper(root.right)

            if left + right + mid >= 2:  # 说明就是我们想要的
                self.flag = root
            return mid or left or right

        helper(root)
        return self.flag

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n5.left = n7

foo = Solution()
foo.lowestCommonAncestor(n1,n6,n7)
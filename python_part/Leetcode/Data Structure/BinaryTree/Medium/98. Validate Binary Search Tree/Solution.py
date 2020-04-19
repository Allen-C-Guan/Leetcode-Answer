# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
这个解法不过就是用inorder来遍历，然后看是不是升序且没有重复的元素

检验一个list中是否有相同元素的方法！！
len(list) == len(set(list))

'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        array = []
        def helper(root:TreeNode):
            if root is None:
                return
            helper(root.left)
            array.append(root.val)
            helper(root.right)
        helper(root)
        return array == sorted(array) and len(array) == len(set(array)) #对比长度


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

foo = Solution()
print(foo.isValidBST(n1))
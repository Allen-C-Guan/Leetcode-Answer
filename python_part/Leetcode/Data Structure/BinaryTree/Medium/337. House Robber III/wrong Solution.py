# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
这个思路是错的！！！
该思路相当于默认了，要拿就要拿一层，但是事实并非如此！！！！

'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        grad_father = father = res = 0
        cur_level = [root]
        while cur_level:
            cur_val = 0
            next_level = []
            for cur_node in cur_level:  #获取当前level的和，和下一层level的所有node
                cur_val += cur_node.val
                if cur_node.left is not None: next_level.append(cur_node.left)
                if cur_node.right is not None: next_level.append(cur_node.right)
            res = max(father, grad_father+cur_val)  # dp问题，二选一
            grad_father, father = father, res   #update  注意的是把最优解更新给father，而不是当前层的值
            cur_level = next_level
        return res



n1 = TreeNode(4)
n2 = TreeNode(1)
n3 = TreeNode(2)
n4 = TreeNode(3)
n1.left = n2
n2.left = n3
n3.left = n4

foo = Solution()
print(foo.rob(n1))



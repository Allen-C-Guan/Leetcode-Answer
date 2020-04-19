# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
这个方法适用于所有二叉树！！ 因为我没有看到是BST，有性质就是 in order遍历的结果就是一个sorted array啊 我wtf！！！
硬是把简单做成了中等。

这个方法超时了，但是是有效的
二叉树的最基本的思路就是：
每一层递归的分支都是3个。分别是 root，left，right。三者之间互相独立的，递归关系要将这三者之间独立出来思考比较好。

'''
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        greater_tree = self.buildGreater(root, root)
        return greater_tree

    def buildGreater(self, root, head):
        if root is None:
            return

        greater_node = TreeNode(self.__preOrder(root.val, head) + root.val)
        greater_node.left = self.buildGreater(root.left, head)
        greater_node.right = self.buildGreater(root.right, head)
        return greater_node

    def __preOrder(self, cur_value, root):
        if root is None:
            return 0
        res = root.val if root.val > cur_value else 0
        left = self.__preOrder(cur_value, root.left) #左子数中大于cur_value 的值的和
        right = self.__preOrder(cur_value, root.right) #右子数的值大于cur_value的值的和
        return left + right + res  #左右子树和包括自己在内的上层中一共大于cur——value的值
    '''
    这里递归分析要看2层即可。
    root当前的值 = left + right + res
    那么 right和left是否也符合这个规律，如果符合这个规律，那么说明递归关系是正确的。
    
    检查递归出口：
    如果当前节点是None，那么说明上层的right或者left将有0出现。这符合规律 递归出口也是正确的
    
    '''


n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(13)


n1.left = n2
n1.right = n3


foo = Solution()
foo.convertBST(n1)
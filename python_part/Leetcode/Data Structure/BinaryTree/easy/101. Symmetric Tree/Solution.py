# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
该方法有问题！！！！！！！！
in order的方法并不能过审，因为in order并不是一个审查symmetry有效的方法，有些特殊的情况，总是会有 in order的序列是对称的，但是其树本身不是对称的

如果想要用该方法，可以改进一下，左边的value*-1， 右边的value*1，这样list中的值就是与左右子树相关的了。
但是我懒得改了

'''

'''
分析一下这个问题：

对于二叉树的检测，不妨用一种方式去遍历二叉树，而后得到一个list，我们只需要检查list是否是对称的就好。

而这个travel order就是  
     in order !!!!

in order的实现方法：
    递归：
        if T is not empty
        return T.left
        visit T           由于是递归，只有T.left为none的时候， T才会被visit
        return T.right    由于是递归， 只有 T和T.left 全都没有了的时候， T right subtree才会被travel
 
'''

'''


'''




class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        global data_list
        data_list = []
        self.inOrder(root)
        length = len(data_list)
        for i in range(int(length / 2)):
            if data_list[i] != data_list[length - 1 - i]:
                return False
        return True

    def inOrder(self, root: TreeNode):
        if root is not None:
            self.inOrder(root.left)
            #这个递归不能加return， 递归中return只有两种情况下才有，1 递归出口， 当前括号的结果，这个题中，很明显，不需要每个括号要有结果，括号内已经完成了内容
            # 如果有了return，则意味着括号结束！！！

            if (root.right is None and root.left is not None) or (root.right is not None and root.left is None):
                if root.right is None:
                    data_list.append(root.val)
                    data_list.append(None)
                else:
                    data_list.append(None)
                    data_list.append(root.val)
            else:
                data_list.append(root.val)



            self.inOrder(root.right)

        return #这才是括号的结尾


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(0)
t4 = TreeNode(3)
t5 = TreeNode(4)

t1.left = t2
t1.right = t3
t2.right = t4
t3.left = t5




foo = Solution()
print(foo.isSymmetric(t1))
print(data_list)

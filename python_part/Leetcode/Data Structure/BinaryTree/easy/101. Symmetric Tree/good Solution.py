class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
        这里我们为什么要用两个递归函数？
        首先 递归要有递归出口和递归公式。 

            递归公式为：
            若判定T为root的树是否是对称的，需要判定：

            若判定以T为给定的root的两个子树，T.left and T.right 之间是否是对称的，这需要迭代的判定：

            T.left.left == T.right.right && T.left.right == T.right.left &&  T.left == T.right  

            而这个迭代可以用 


            因此递归出口应该为递归的最基本情况 或 递归的终止条件：（详见onenote）
                1。递归的最基本情况：
                    1）没有子树了，left == right == None 此时应该return true

                2。递归终止条件：（return false）
                    1) 子树的个数不成对了， (left == None and right != None) or (left != None and right == None)
                    2）left != right

'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.right, root.left)

    def isMirror(self,right:TreeNode, left:TreeNode):
        if right is None and left is None:
            return True

        if right is not None and left is not None:
            if right.val != left.val:
                return False
            pair1 = self.isMirror(right.right, left.left)
            pair2 = self.isMirror(right.left, left.right)
            return pair1 and pair2

        return False







t1 = TreeNode(0)
t2 = TreeNode(1)
t3 = TreeNode(2)
t4 = TreeNode(3)
t5 = TreeNode(4)
t6 = TreeNode(5)
t7 = TreeNode(6)

t1.left = t2
t1.right = t3
t2.right = t4
t3.left = t5
t4.left = t6
t5.right = t7




foo = Solution()
print(foo.isSymmetric(t1))







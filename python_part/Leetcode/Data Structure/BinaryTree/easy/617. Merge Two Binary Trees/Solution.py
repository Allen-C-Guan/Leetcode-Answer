# Definition for a binary tree node.
'''
如何使用递归来连接tree？
流程是这样的：
1。建立一个新的node。  在递归开始的时候，建立一个新的node，此时是一个孤立的node
2。在递归结尾的时候要返回这个孤立的node
3。但在递归的上层，该递归赋值给了root的left 或者 right  此时孤立的node就和上层建立了联系。

因此这里，我们建立联系的方法是把新node在递归后与上一级建立联系。只有返回时候才建立联系

代码实现是：
1. 建立newNode。（只关心当前位置的值）
2. 递归 （关心childern的值）
        left = self.buildNode(*)
        right = self.buildNode(*)
3. 返回：（说明当前位置及以下的全部内容，都处理完成了。）
        return newNode
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            newNode = t2
        elif t2 is None:
            newNode = t1
        else:
            newNode = TreeNode(t1.val + t2.val)
            '''
            每次都只创建一个全新的没有任何关联的新node，且只关心当前的点，
            那么如何将新node和之前的node联系在一起呢？
            就靠的是return和left = self.mergeTrees来建立联系 
            '''
            newNode.left = self.mergeTrees(t1.left, t2.left)
            newNode.right = self.mergeTrees(t1.right, t2.right)
        return newNode



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n1.left = n2
n1.right = n3
n2.left = n4


m10 = TreeNode(10)
m20 = TreeNode(20)
m30 = TreeNode(30)
m70 = TreeNode(70)
m40 = TreeNode(40)

m10.left = m20
m10.right = m30
m30.left = m70
m30.right = m40


foo = Solution()
foo.mergeTrees(n1,m10)


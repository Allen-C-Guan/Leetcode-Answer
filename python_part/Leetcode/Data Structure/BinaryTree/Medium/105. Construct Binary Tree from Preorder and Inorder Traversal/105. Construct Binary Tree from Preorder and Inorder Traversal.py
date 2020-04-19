'''
这里的思路很好想：就是利用pre-order 来找root，把该root定位在in order里面。那么其在inoder里面的左边就都是左子树，右边的就都是右子树。

可是实现这个前提是，要准确的找到 左右子树在pre-order和in-order的分布与其之间的关系：
pre-order: root， (left-subtree-list)，(right-subtree-list)
in-order: (left-subtree-list)， root， (right-subtree-list)

我们假设left-subtree的长度为 len_left
则我们会发现：
                pre-order  |  in-order
root:              0       |   len_left
leftsub:      1:len_left   |  0:len_left-1
rightsub    len_left+1:end |  len_left+1:end

我们发现 inorder和preorder的右子树有相同的位置  左子树错位一个位置


而这就递归关系！！！
我们用preorder来找root
用inorder来计算左子树的长度。
利用计算出来的左子树的长度，定位preorder中，左右子树的位置

就这样
我们不停的把inorder 和 preorder按着左右子树来拆分。就可以得到真实的子树了

递归的实现：
我们根本不需要记录之前的root，因为我们采用的是正向的逻辑。


我们的逻辑是：
1. 建立当前节点：
2. 建立左右节点：递归的执行机制就在于一下到底。只有左右子树完全都执行完了，才会执行下一句
3. 返回当前节点 ：这也意味着，只有当左右节点包括内部完全都完成了以后才会return当前节点
但是正向逻辑需要每层递归有return，return当前的node。这样你就可以写left = self.findRoot(*)
'''

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        return self.findRoot(preorder,inorder)

    def findRoot(self, preorder: List[int], inorder: List[int]):

        if len(preorder) < 1:
            return None # 没有子树了
        root_node = TreeNode(preorder[0])

        lefttree_len = inorder.index(root_node.val)  # 就是真实的leftsubtree的长度
        root_node.left = self.findRoot(preorder[1: lefttree_len+1], inorder[:lefttree_len])
        root_node.right = self.findRoot(preorder[lefttree_len+1:], inorder[lefttree_len+1:])
        return root_node


foo = Solution()
foo.buildTree([3,9,20,15,7],[9,3,15,20,7])







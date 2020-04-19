
'''
本题思路：
该方法采用最好思考的方法，就是把所有节点都当成一遍root，然后计算一遍符合条件的个数。
'''

'''
再强调一遍！
写递归的思路：
1. 首先明确递归要实现的功能
2. 递归关系。如何利用该递归的功能，将得到的子问题的结果合成得到当前问题结果 并保证所有节点都满足该递归关系
3. 关系递归出口的具体分类讨论和具体的结果

我们不需要关心除了出口之外的任何一层递归的具体数值是多少。数值我们只关心出口处。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:  # 功能是找开头
        res = 0 if root is None else self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return res

    def findPath(self, root, sums) -> int:  # 找到以root开头的path的条数
        if root is None: return 0
        cnt = 1 if sums - root.val == 0 else 0
        return self.findPath(root.left, sums - root.val) + self.findPath(root.right, sums - root.val) + cnt

    '''
    这里的递推关系的检验和上一道题相似：
    递归关系为 left + right + 自身
    
    那么递归的底是什么呢？（递归出口）
    那就是None的出现。
    如果None出现了，那么返回的应该是0，表示以None为head的符合条件的个数为0条。
    
    '''
    '''
    我们可以发现，在递归的过程中，我们采用的是 cur = left + right + cur 的方法
    这就和fib(i) = fib(i-1) + fib(i-2) 是一样的
    其复杂度是很大的。
    
    对于类似fib问题的问题。我们采用多项式和的方法，即。用回朔法，用一个list来记录目前为止的和，然后用和直接和当前的值做比较。
    这样遍历一遍二叉树就可以得到结果。
    '''
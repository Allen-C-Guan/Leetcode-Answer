# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
写递归还是那个最重要思路：
在写递归的时候，一定要时刻记得，子问题已经被我的递归解决掉了。我不要去考虑如何去解决子问题的事情。我要做的就是如何利用子问题搞好当前的问题。

那么子问题到底怎么去得到？ 我们只考虑递归出口处的最基本的子问题的结果就行了。其他非最基本子问题都会自然得以解决。
'''


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:  # 递归功能判定当前位置及以下是否是相同的
        if p is None and q is None: return True      # 若q和p都是None，说明都到底了。而且还是相同的
        if p is None or q is None: return False      # 有且只有一个是None，不用继续判定了，直接就是False
        return q.val == p.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
                                                    # 剩下的是q和p都不是none的情况 需要左右子树都是相同的，自己也相同才是相同的

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
连queue都不用，就用两个list，一个记录当前level，一个记录下一层的level，每次把当前level的最后一个node的值放到res就行了
'''
from typing import List
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        cur_level, res = [root], []
        while cur_level:
            next_level = []
            res.append(cur_level[-1].val)
            for cur_node in cur_level:
                if cur_node.left: next_level.append(cur_node.left)
                if cur_node.right: next_level.append(cur_node.right)
            cur_level = next_level
        return res

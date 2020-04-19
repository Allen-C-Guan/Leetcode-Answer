'''
DP算法
i give it up!!!!!

这个题只能用递归，妈的！！！ 因为dp的情况太复杂了。

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def generateTrees(self, n: int):
#
#         dp = [[[] for _ in range(n)] for _ in range(n)]
#         dp[0][0].append([TreeNode(1)])
#
#
#
#
#         for start in range(n):
#             for end in range(start+1,n):
#                 #build dp[start][end]
#                 for root in range(start,end+1):
#                     for left in dp[start][root-1]:
#                         for right in dp[root+1][end]:


#
# foo = Solution()
# a = foo.generateTrees(3)
# print(a)
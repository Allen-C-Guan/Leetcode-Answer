"""
这个程序最大的问题在于，并不是从stack里面随便pop出来一个相同的元素就可以完成匹配，当相同元素出现的时候，需要小心抉择pop哪一个，后面才有机会成功匹配。

而这个所谓的小心抉择pop哪一个就是这个题最难的点。
而这和之前最大矩形的题的keypoint有些相似，在最大矩形中，最麻烦的问题在于当横向 纵向或者斜着组成的矩形面积相同时，要小心选择记录哪个。

"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        stack1 = [_ for _ in s1]
        stack2 = [_ for _ in s2]

        for e in s3:
            if len(stack1) != 0 and e == stack1[0]:
                stack1.pop(0)
            elif len(stack2) != 0 and e == stack2[0]:
                stack2.pop(0)
            else:
                return False


        if len(stack1) == len(stack2) == 0:
            return True

        else:
            return False

foo =Solution()
print(foo.isInterleave(
"aabcc",
"dbbca",
"aadbbcbcac"))
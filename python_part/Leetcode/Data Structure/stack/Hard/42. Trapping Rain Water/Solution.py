from typing import List
'''
这个问题一看又是一个遮挡问题。需要用到单调堆栈的帮忙。
这种类型题最大的特点在于，遮挡。
我们用水平面的高度不同来对整段进行分段讨论。
首先若水平面高度不同，则必有同一水平面的两端的两个柱子的最小值是不同的。且水平面中间的柱子均小于两端柱子的最小值。

设两端柱子分别是A和B

这道题可以发现，如果A在左边，B在右边， A <= B，且A和B之间的元素都小于A。那么我们会发现， B右边是任何值，对于A和B之间元素没有任何影响。
即A和B之间的元素的头顶上水平面的高度均是A。那么每个元素e头上的存水量就是 A-e。

于是我们的目标就变成了寻找每段的端点柱子A和B。
我们采用单调栈，栈中只存放更大的值。若新加入的值小于栈顶，拒绝加入，并累计当前存水量。若大于，则让其加入。

可是我发现，堆栈既然只用到栈顶，那不如不要了。

但是我们发现这个方法只能解决最大值左右两边一半的问题。
那我们直接就从两端开始，向中间，最大值处会和就行了。

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        def buildStack(height_list):
            max_height, res = 0, 0
            for cur_h in height_list:
                if cur_h >= max_height:  # 这时候不存水
                    max_height = cur_h
                else:  # 这时候存水
                    res = res + (max_height - cur_h)
            return res
        max_index = 0
        for i in range(len(height)):  # 找到最右边的最大值
            if height[i] >= height[max_index]:max_index = i
        max_index = min(max_index,len(height)-1)
        return buildStack(height[:max_index+1]) + buildStack(reversed(height[max_index+1:]))


foo = Solution()
print(foo.trap([0,1,0,2,1,0,1,3,2,1,2,1]))




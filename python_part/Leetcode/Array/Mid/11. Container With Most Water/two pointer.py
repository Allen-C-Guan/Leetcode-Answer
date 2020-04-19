'''
该问题是一个典型的缩减搜索范围来减少计算的问题

双指针法：
若将双指针分别从两端向中间靠近的方法来寻找可能解。


若当前两端指针i和j，对应的函数值分别是 a和b，且a > b，则面积公式为 (j-i)*min(a,b) = (j-i)*b
移动分两种：
1. 向内移动大的（a）,即指针i，我们得到了新的值 c，此时面积公式为 (j-i-1)*min(c,b) < (j-i)*b 恒成立
        因为min(c,b) <= b 恒成立，说人话叫，即使c比a大，又有什么用，不但没有增加桶高，还把底给缩短了
2. 向内移动小的（b），即指针j，我们得到新的值d，此时面积为：(j-i-1)*min(a,d)，
        由于min(a,d)是有可能大于b的，因此上式是有可能 大于(j-i)*b的

综上所述：
我们在寻找更大面积的过程中，如果把较大的端点向内收缩，对增加容积没有任何帮助。因为本来耽误容积的也不是大的端点
因此，只有把短的端点向内收缩才有可能出现更大的容积。

本质上，我们通过对该数学问题的分析，根据该数学问题的特点，我们缩小了可能答案的搜索范围


'''

class Solution:
    def maxArea(self, height) -> int:
        size = len(height)
        left = 0
        right = size - 1
        max_area = 0

        while left < right:
            max_area = max((right - left) * min(height[left], height[right]), max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area



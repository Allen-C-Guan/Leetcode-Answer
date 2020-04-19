from typing import List
'''
超时！
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for left in range(len(heights)):
            cur_min = heights[left]
            for right in range(left, len(heights)):
                cur_min = min(cur_min,heights[right])
                max_area = max(max_area,cur_min * (right - left + 1))
        return max_area




'''
思路没得问题，问题是超时了。
'''

class Solution:
    def maxArea(self, height) -> int:
        max = 0
        for start in range(len(height)):
            for end in range(start+1, len(height)):
                volumn = (end - start) * min(height[start], height[end])
                if volumn > max:
                    max = volumn

        return max

foo = Solution()
print(foo.maxArea(
[1,8,6,2,5,4,8,3,7]))
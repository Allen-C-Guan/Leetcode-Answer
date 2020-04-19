from typing import List
'''
思路还是基于：寻找最大重复长度。即两个while循环的嵌套，需要注意几个点
1. cnt从1开始.
2. 内循环更新counter。循环的条件是既相同也要不超过最后的位置
3. 外循环更新pointer，

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = len(nums)
        pointer = 0
        while pointer < res:
            cnt = 1
            while pointer+cnt < res and nums[pointer+cnt] == nums[pointer]:
                cnt += 1

            if cnt > 1:
                move = cnt - 2
                for i in range(pointer+cnt, res):
                    nums[i-cnt+2] = nums[i]
                res -= move
                pointer += 2
                continue
            pointer += 1
        return res

foo = Solution()
print(foo.removeDuplicates([]))




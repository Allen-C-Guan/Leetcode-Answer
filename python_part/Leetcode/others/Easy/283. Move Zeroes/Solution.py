from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        size = len(nums)
        if size == 0:
            return []
        pointer = 0
        end = size-1  #end 指向最后一个不是0的位置
        while pointer < end+1:
            cnt = 1
            if nums[pointer] == 0:
                while cnt+pointer < end+1 and nums[pointer+cnt] == 0:
                    cnt += 1  # cnt + pointer 指向的是第一个不是0的位置

                for i in range(pointer, end-cnt+1):
                    nums[i],nums[i+cnt] = nums[i+cnt],nums[i]
                end -= cnt
                pointer += 1
                continue
            pointer += cnt
        print(nums)

        
foo = Solution()
foo.moveZeroes(
[4,2,4,0,0,3,0,5,1,0] )



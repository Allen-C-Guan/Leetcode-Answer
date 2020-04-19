'''
这个问题的难点在于 in-place.

该问题的技巧在于，找到以后可以直接向前覆盖，却永远不会覆盖掉还没被找到的element，这是因为sorted和duplicated特性导致的。
'''


class Solution:
    def removeDuplicates(self, nums) -> int:

        pointer = 0

        for i in range(len(nums)):
            if nums[i] > nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]

        return pointer + 1


foo = Solution()
input = []
print(foo.removeDuplicates(input))
print(input)

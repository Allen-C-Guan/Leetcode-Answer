
'''
该题最大的问题在于如何处理两个for循环的重复问题。
我们要让重复的部分，至少执行一次循环，然后再跳过!。

这里，"至少执行一次" 这个逻辑非常重要， 至少执行一次中的一次是第一个一次。这一次必须要执行，且后面的重复的不要执行。
执行一次是为了保证不漏下，而后面不执行是为了不重复。

那么 for循环如何保证至少一次？  那就是第二个for循环不要跳过第一次进入的for循环。但是要跳过之后的重复。
而第一次进入第二个for循环的特点就是 p2 = p1 + 1 这一次，不管重复与否，我们都要执行下去。

为什么在双指针部分我们不需要如此麻烦？
因为在双指针部分，我们用的是while循环，而while循环至少执行一次，不管重复与否！！！ 而for循环，如果你不用if判定来跳过，你就挨个执行。
可你用了if跳过呢？ 他又有可能一次都不执行！


'''

class Solution:
    def fourSum(self, nums, target: int):
        res = []
        nums = sorted(nums)
        size = len(nums)

        for p1 in range(size-3):
            if p1 > 0 and nums[p1-1] == nums[p1]:continue
            for p2 in range(p1+1, size-2):                          #这两个for循环也要避免重复啊,只要是指针，就要避免重复，而避免重复的方法就是向上一项看齐
                if p2 != p1+1 and nums[p2-1] == nums[p2] : continue       #这里边界条件必须是1，因为我们至少要让该结构体全部执行一遍
                left = p2 + 1
                right = size - 1
                while left < right:
                    tmp = nums[p1] + nums[p2] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[p1], nums[p2], nums[left], nums[right]])
                        right -= 1
                        left += 1

                        while left < right and nums[right] == nums[right+1]:right -= 1
                        while left < right and nums[left] == nums[left-1]:left += 1
                    elif tmp < target:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]: left += 1

                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1

        return res

foo = Solution()
print(foo.fourSum([0,-1,0,1,-2,-5,3,5,0], 6))
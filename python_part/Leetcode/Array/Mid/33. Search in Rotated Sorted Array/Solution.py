'''
二分法的几大要素：
1. 递归出口：
    left > right 和
    mid == target 两个

    这样当left == right的时候，也就是只有一个元素的时候也可以进入到递归出
口。
2. 递归入口处，一定要有
        mid + or - 1

        来保证二分的区域一定会移动，最少也是一个，这样区间才会保证递归一定会从递归出口left>right中出来而不会被卡住


该题的思路：
首先logn就一定要二分法来搜索index
二分法有个缺点，只能利用sorted array。

既然我们想用二分，还想不sorted array 怎么办？

那我们可以通过分类讨论的情况，让可行域一定缩减到一个包含target的有序数列区间中，然后在利用二分法。

那么自然，递归的入口就要分成两个大类：
1. 该区间是个sorted array （这部分就是基本的二分法 很简单）
2. 该区间不是sorted array

分析一下第二类：
当该区间（range_i）不是sorted array的时候， 我们如果取个中间值 mid， 那么 range_i 就被 mid一分为二。
我们设被分成的两个区域分别叫 range_i_left 和 range_i_right.

这两个区域left 和 right，必然有且至少有一个区域是sorted好的，我们只要找到那个sorted好的区域，并用sorted好的区域的端点值来判定target是否在该区域。
如果不在该区域，那么我们就在另一半寻找

我们为什么这么做， 因为只有一个完全sorted 的区域才有这么好的性质，即端点值判定所期望的值是否在该区域
'''

class Solution:
    def search(self, nums, target: int) -> int:
        return self.getIndex(nums, 0, len(nums)-1, target)

    def getIndex(self, nums, left, right, target):
        #递归出口
        if left > right:
            return -1
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        #递归入口
        if nums[left] < nums[right]:
            if nums[mid] > target:
                return self.getIndex(nums, left, mid-1, target)
            else:
                return self.getIndex(nums,mid+1,right, target)

        else: # 拿到的部分是乱序的，但中间分开，总会有一边是正序的把
            if nums[left] <= nums[mid]:  #如果左半边是正序
                if nums[left] <= target <= nums[mid]:
                        # 如果target在这段正序之中的话，那就就返回这段, 这里边界也要带上，
                        # 因为在进入到这个区域中的时候，你并没有确定该区域的端点是否与target相同
                    return self.getIndex(nums, left, mid-1, target)
                else:
                    return self.getIndex(nums, mid+1, right, target)
            else: # 右半边是正序
                if nums[mid] <= target <= nums[right]: #如果target没有在这段正序中，那就返回别的段
                    return self.getIndex(nums, mid+1, right,target)
                else:
                    return self.getIndex(nums, left,mid-1,target)
foo = Solution()
print(foo.search([1,3,1,1,1],3))
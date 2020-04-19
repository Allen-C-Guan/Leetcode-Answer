from typing import List
'''
旋转序列使用二分法的关键在于：使用正序部分来判定是否在其区间内。
这是由于 二分之后，至少有一个区域是正序的，而正序的可以利用端点来判定

但是这里由于可以出现重复的内容，因此我们会出现 nums[left] == nums[mid]的情况（由于是旋转造成的，如果left==mid = a 则说明mid之后也都是相同的元素a）

这时候，你观察发现 left == right == mid ，也就是说你通过观察这三个点，你丝毫无法判定在哪个区域。这时候怎么办？？？ 

通过移位，去掉迷惑项！
只要让left右移一位即可！
因为你肯定是在想，既然无法判定，不如我们想办法避开，通过移位就可以避开。

为什么是left右移动一位，而不是right左移一位呢？ 
因为你的判定条件是判定mid， 而mid是向左靠近的。因此一定不会发生判定left是否正确之前，就移动了left的情况。可是right就不一定了，当只有两个元素的时候
left == mid 这时候，如果你移动了right，那么right还没有被判定就移动了！




'''





class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self.binarySearch(0,len(nums)-1, nums,target)

    def binarySearch(self, left: int, right: int, nums: List[int], target: int) -> bool:
        if left > right: # 递归出口1： 边界条件退出
            return False
        mid = int((left+right)/2)

        if nums[mid] == target: # 递归出口2，找到退出
            return True

        if nums[left] < nums[right]: # 一定是正序 正常二分
            if nums[mid] < target:
                return self.binarySearch(mid+1, right, nums, target)
            if nums[mid] > target:
                return self.binarySearch(left,mid-1,nums,target)

        else:
            if nums[left] < nums[mid]:# 如果前面是正序的话：
                if nums[left] <= target < nums[mid]:
                    return self.binarySearch(left,mid-1,nums,target)
                else:
                    return self.binarySearch(mid+1,right,nums,target)
            elif nums[left] > nums[mid]: # 如果后面是正序
                if nums[mid] < target <= nums[right]:
                    return self.binarySearch(mid+1,right,nums,target)
                else:
                    return self.binarySearch(left, mid-1, nums, target)
            else: # nums[left] == nums[mid] 这个时候你就分不清了！！！！
                return self.binarySearch(left+1, right,nums, target)



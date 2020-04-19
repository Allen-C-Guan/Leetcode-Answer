'''
本题思路有两大难点：
1. 如何用二分来实现区域的查找
2. 如何设置递归出口

对于第一个问题：
我们可以分两次递归！ 一次递归是为了左端点，一次递归是为了找右端点。
这是因为二分法是通过夹逼来实现查找，而夹逼只能确定一个点，因此只能分两次去分别找两个端点
logn，因此我们依然会用二分法来解决这个问题。可是与之前的二分法不同，我们找的是端点，而不是某一个值。
二分法的目标不同，如果二分用递归来实现，那么意味着递归出口不同。我们需要把递归出口设置成为端点退出，而不是找到target就推出。

为了实现端点退出，我们应该如何设置递归出口，这是这个问题的关键中的关键。
若我们设，当前被二分的区间的3个重要节点分别是， left mid  right.
我们对mid分类讨论：
当mid ！= target的时候， 那就正常二分法
当mid == target的时候，分成2种情况，
    1。mid就在端点处。（若是左端点，此时有 nums[mid]== target, nums[mid-1] != target)
    2。mid不在端点处。

    对于mid不在端点处，可以把这种情况融入到二分法中。
    mid在端点处，那就让mid直接退出就好了。


'''

class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]

        return [ self.getLeft(nums, 0,  len(nums)-1, target), self.getRight(nums,0,len(nums)-1, target)]

    def getLeft(self, nums, left, right,target):
        #递归出口
        if left >= right:
            return left if nums[left] == target else -1

        mid = int((left+right)/2) #这里mid应该是向左靠的
        if nums[mid] == target and nums[mid-1] != target:
            return mid
        # 递归入口
        if nums[mid] < target:
            return self.getLeft(nums,mid+1, right,target)
        else:
            return self.getLeft(nums,left,mid-1,target)

    def getRight(self,nums,left,right,target):
        if left >= right:
            return left if nums[left] == target else -1
        mid = int((left + right) / 2)  # 这里mid应该是向左靠的

        if nums[mid] == target and nums[mid+1]!=target:
            return mid
        if nums[mid] > target:
            return self.getRight(nums,left,mid-1,target)
        else:
            return self.getRight(nums,mid+1,right,target)


foo = Solution()
foo.searchRange([5,7,7,8,8,10],7)
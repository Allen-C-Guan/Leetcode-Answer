'''
quick select的方法 也是quicksort的基础
我们使用递归来完成

'''
from typing import List

class Solution:
    def __init__(self):
        self.res = None
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # 其实这个partition 由于采用的是lo，hi，并不需要计算k的相对大小。
        # 在partition里面，我们最好还是每次随机选择pivot比较快。
        # s 表示slow，fast 不停的走， slow只有被替换了以后才走
        '''
        for fast in range(lo,hi):
            if num[fast] < pivot:
                swap num[fast] num[slow]
                slow += 1
        slow -= 1
        swap nums[lo] num[slow]
        '''
        def partition(nums: List[int], lo, hi):
            pivot, s = nums[lo], lo+1        # s永远指向的是前面的大于pivot的数的前一个
            for fast in range(lo+1, hi+1):
                if nums[fast] > pivot:       # 这里是 > 则得到的就是逆序， s就会停在小的上面，
                    nums[fast], nums[s] = nums[s], nums[fast]
                    s += 1
            s -= 1
            nums[lo], nums[s] = nums[s], nums[lo]
            return s

        def quickSelect(nums: List[int],lo,hi,k):  #与二分的逻辑相同, 先判定，再二分
            s = partition(nums,lo,hi)
            if s == k-1:
                self.res = nums[s]
            else:
                if s < k-1: quickSelect(nums,s+1,hi,k)
                else:quickSelect(nums,lo,s-1,k)

        quickSelect(nums,0,len(nums)-1,k)
        return self.res

foo = Solution()
print(foo.findKthLargest([3,2,3,1,2,4,5,5,6],4))

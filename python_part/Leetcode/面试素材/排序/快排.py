from typing import List
def partition(nums: List[int], lo, hi):
    pivot, s = nums[lo], lo + 1              # s永远指向的是前面的大于pivot的数的前一个
    for fast in range(lo + 1, hi + 1):
        if nums[fast] < pivot:               # > 逆序, < 正序 ， s就会停在小的上面，
            nums[fast], nums[s] = nums[s], nums[fast]
            s += 1
    s -= 1
    nums[lo], nums[s] = nums[s], nums[lo]
    return s

def QuickSort(arr:List,lo, hi):
    if lo < hi:                           # 分不可分就结束
        s = partition(arr,lo,hi)          # 用s将array一分为二
        QuickSort(arr,lo,s-1)             # 左边继续拆分
        QuickSort(arr,s+1,hi)             # 右边继续拆



res = [5,4,3,2,1]
QuickSort(res,0,len(res)-1)
print(res)
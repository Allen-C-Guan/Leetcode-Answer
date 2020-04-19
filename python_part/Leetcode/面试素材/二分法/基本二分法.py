from typing import List

# 迭代的方法
def binarySearch(arr:List, target:int):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = int((left+right)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

# print(binarySearch([0, 1,2,3,4,5,6], 7))

# 递归的方法
def recursiveBinarySearch(arr:List, left, right, target):
    if left > right:
        return -1
    mid = int((left+right)/2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursiveBinarySearch(arr, left, mid-1, target)
    else:
        return recursiveBinarySearch(arr, mid+1, right,target)

print(recursiveBinarySearch([0,1,2,3,4,5,6], 0, 6,0))
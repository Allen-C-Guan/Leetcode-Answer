from typing import List
def insertionSort(arr:List):
    for cur in range(len(arr)):
        temp = arr[cur]
        left = cur - 1
        while left >= 0 and arr[left] > temp:
            arr[left+1] = arr[left]
            left -= 1
        arr[left+1] = temp
    return arr

print(insertionSort([5,4,3,2,1]))

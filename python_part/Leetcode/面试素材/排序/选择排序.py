from typing import List
def selectionSort(arr:List):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):  # 选择最小的
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i] # 交换
    return arr
print(selectionSort([5,4,3,2,1]))

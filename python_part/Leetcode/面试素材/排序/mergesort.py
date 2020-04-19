from typing import List
def merge(B:List, C:List, A:List):
    i = j = k = 0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    # 处理剩余元素
    if i == len(B):
        A[k:] = C[j:]
    else:
        A[k:] = B[i:]

def mergeSort(A:List):
    if len(A) > 1:
        B = A[:int(len(A)/2)]  #二分array
        C = A[int(len(A)/2):]
        mergeSort(B)   # 二分后的array排序
        mergeSort(C)
        merge(B, C, A) #两个array merge起来

arr =[5,4,3,2,1]
mergeSort(arr)
print(arr)
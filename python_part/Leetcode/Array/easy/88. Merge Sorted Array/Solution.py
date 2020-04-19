# MergSort中的merge
"""
keypoint:
in-place!!
由于in-place的存在，使得merge变得复杂。


解题思路：
使用三个pointer分别表示 已经完成的部分， nums1中已经完成的部分， nums2中已经完成的部分
1.倒着排序
2.如果是nums1 中的则swap
3.如果是nums2中的，则覆盖即可
4.如果nums1中先排完了，则把剩余的nums2补进去，如果是nums2排完了，剩余的nums1自动排好

"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:

        '''
        需要考虑特殊情况 即 m = 0 时，这时就是简单的copy
        '''
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]



        i = m - 1  # num1 pointer
        j = n - 1  # num2 pointer
        p = n+m-1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[i], nums1[p] = nums1[p], nums1[i]  # swap 的简单写法！！！ a, b = b, a
                i = i - 1
            else:
                nums1[p] = nums2[j]
                j = j-1

            p = p-1

        '''
        如果是nums1先被排完了(i == -1)，那nums2才可能被剩下，这时需要复制剩余nums2到nums1的最前面。
        而如果nums2被排完了，则nums1剩下的自动就保持原位即可。
        '''
        if i == -1:
            for rest_num in range(j+1):
                nums1[rest_num] = nums2[rest_num]
foo = Solution()

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

foo.merge(nums1,m,nums2,n)
print(nums1)
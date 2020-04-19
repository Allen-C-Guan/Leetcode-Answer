class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:]= sorted(nums1[:m] + nums2)



foo = Solution()

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

foo.merge(nums1, m, nums2, n)
print(nums1)

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        path = []
        nums.sort()
        self.__DFS(nums, path, res)
        return res

    def __DFS(self, nums, path, res):
        path = path.copy()


        if len(nums) == 0:
            res.append(path)
            return
        # 这里因为我们用的是index来索引，因此，必须保证array是保序的
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                cur = nums[i]
                path.append(cur)
                nums.remove(cur)
                self.__DFS(nums, path, res)
                nums.append(cur)
                nums.sort()
                path.pop()

foo = Solution()
print(foo.permuteUnique([1, 2, 3]))

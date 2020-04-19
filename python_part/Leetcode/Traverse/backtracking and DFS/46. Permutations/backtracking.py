from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums.sort()
        path = []
        res = []
        self.__DFS(nums, path, res)
        return res

    def __DFS(self, nums, path,res):
        path = path.copy()
        # 递归出口
        if len(nums) == 0:
            res.append(path)
            return
        # 递归入口
        for i in nums:
            path.append(i)
            nums.remove(i)
            self.__DFS(nums, path, res)
            nums.insert(0, i)  #你给人家删了，还要给人家加回来
            path.pop()

foo = Solution()
print(foo.permute([1,2,3]))

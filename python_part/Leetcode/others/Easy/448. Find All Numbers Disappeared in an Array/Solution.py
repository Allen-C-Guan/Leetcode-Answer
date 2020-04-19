from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        full_set = {_ for _ in range(1,size+1)}
        for i in nums:
            full_set.discard(i)
        return list(full_set)

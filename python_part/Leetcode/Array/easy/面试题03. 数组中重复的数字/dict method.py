from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0)+1
            if map[n] > 1: return n

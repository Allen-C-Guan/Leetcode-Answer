from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) == 1:
            stones.sort()
            stones.append(abs(stones.pop()-stones.pop()))
        return stones[-1]


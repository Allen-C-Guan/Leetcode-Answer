from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest_gas = [gas[i] - cost[i] for i in range(len(cost))]
        for start in range(len(cost)):
            if rest_gas[start] >= 0:
                rest = 0
                for cur in range(start, start+len(cost)):
                    rest += rest_gas[cur%len(cost)]
                    if rest < 0: break
                if rest >= 0:
                    return start
        return -1

foo = Solution()
print(foo.canCompleteCircuit([2], [2]))
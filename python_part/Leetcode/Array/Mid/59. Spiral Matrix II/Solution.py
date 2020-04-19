from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        cnter = 1
        for layer in range(int(n/2)):
            length = n-layer*2-1
            for cnt in range(length):
                res[layer][layer+cnt] = cnter
                res[layer+cnt][n-layer-1] = cnter + length
                res[n-layer-1][n-layer-cnt-1] = cnter + length * 2
                res[n-layer-cnt-1][layer] = cnter + length * 3
                cnter += 1
            cnter = cnter + length * 3
        if n%2: res[int(n/2)][int(n/2)] = n ** 2
        return res


foo = Solution()
print(foo.generateMatrix(3))
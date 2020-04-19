from typing import List
'''
这个直接法超时啊
'''
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        i = j = 0
        obstacles = set(map(tuple,obstacles))
        while i <= x and j <= y:
            for c in command:
                if c == "U": j += 1
                else: i += 1
                if (i, j) in obstacles: return False
                if i == x and j == y:return True
        return False
foo = Solution()
print(foo.robot("URR",[[2,3]],3,2))
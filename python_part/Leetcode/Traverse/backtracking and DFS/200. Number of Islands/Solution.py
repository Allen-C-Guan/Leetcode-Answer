from typing import List
'''
DFS在拓扑中，本就可以用来测试有多少个相对隔离的点。 通过观察DFS的开头次数，即可以得到相互孤立的区域一共有多少个。
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:return 0
        cnt, x_size, y_size = 0, len(grid), len(grid[0])
        for x in range(x_size):
            for y in range(y_size):
                if grid[x][y] == "1":
                    cnt += 1
                    self.infect(x, y, grid)
        return cnt

    '''
    其实这里本质上用的还是DFS。不断的通过感染的方式来将小岛全部感染为0
    '''
    def infect(self, x, y, grid: List[List[str]]):
        grid[x][y] = "0"
        if x - 1 >= 0 and grid[x - 1][y] == "1": self.infect(x - 1, y, grid)
        if x + 1 < len(grid) and grid[x + 1][y] == "1": self.infect(x + 1, y, grid)
        if y - 1 >= 0 and grid[x][y - 1] == "1": self.infect(x, y - 1, grid)
        if y + 1 < len(grid[0]) and grid[x][y + 1] == "1": self.infect(x, y + 1, grid)


foo = Solution()
print(foo.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
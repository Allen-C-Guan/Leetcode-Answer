from typing import List
'''
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
BFS还有一个DFS比不了的优点，就是BFS可以多头同时扩张。
因此，如果你在遍历一个graph的时候，你可以*******轻易找到所有的头*******，那么用BFS一定比DFS要方便
'''
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def findNeighbour(x: int, y: int) -> list:
            neigbor_list = []
            if x+1 < x_size and board[x+1][y] == "O": neigbor_list.append((x+1, y))
            if x-1 >= 0 and board[x-1][y] == "O": neigbor_list.append((x-1,y))
            if y+1 < y_size and board[x][y+1] == "O":neigbor_list.append((x, y+1))
            if y-1 >= 0 and board[x][y-1] == "O": neigbor_list.append((x, y-1))
            return neigbor_list

        if not board: return
        # 找头->所有在边框上的 "O"，并把所有头都压入queue
        queue, x_size, y_size = deque(), len(board), len(board[0])
        for x in range(x_size):
            if board[x][0] == "O": queue.append((x, 0))
            if board[x][y_size-1] == "O": queue.append((x, y_size-1))

        for y in range(y_size):
            if board[0][y] == "O": queue.append((0, y))
            if board[x_size-1][y] == "O": queue.append((x_size-1, y))

        # BFS
        while queue:
            x, y = queue.popleft()
            board[x][y] = "GOOD"
            # 找邻居，把符合条件的邻居拉入queue中。
            queue.extend(findNeighbour(x,y))

        for x in range(x_size):
            for y in range(y_size):
                if board[x][y] == "O": board[x][y] = "X"
                elif board[x][y]=="GOOD": board[x][y] = "O"










from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_list = [set() for _ in range(9)]
        y_list = [set() for _ in range(9)]
        frame_list = [set() for _ in range(9)]

        for x in range(9):
            for y in range(9):
                c = board[x][y]
                if c != ".":
                    if c in x_list[x]: return False
                    if c in y_list[y]: return False
                    if c in frame_list[int(x/3)*3 + int(y/3)]: return False
                    x_list[x].add(c)
                    y_list[y].add(c)
                    frame_list[int(x/3)*3 + int(y/3)].add(c)

        return True

foo = Solution()
foo.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])


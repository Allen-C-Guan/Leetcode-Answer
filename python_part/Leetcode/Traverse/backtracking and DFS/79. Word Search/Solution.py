from typing import List
import copy

'''
deepcopy和copy的区别：
copy只能保证不影响第一层的子类，第二层的子类还是不能保证的
例如这里的board，我们的board是两层list。 那么copy对于第二层内的value，仍然使用的是地址连接

deepcopy则不同，deepcopy使用的却是所有层次的copy

但是问题在于，如果我们用deepcopy，消耗的内存和时间就会超时。
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        break_signal = False
        path_tracking = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    res = self.__DFS(board, word, x, y, path_tracking, break_signal)
                                    # 这里一个重要的privacy leak的问题，即使我们不叫一个名字，但是对于python编译器而言，他不在乎用户名，在乎的只是物理地址。
                                    # 也就说，只要我们把mutable obj作为传入参数了，那么传入的就是一个物理地址而已。就会造成privacy leak
                                    # 如果在DFS中不使用deepcopy，那么path_tracking 的内容就会被篡改。因为path_tracking 是通过两个list嵌套而成，copy无法保证第二层的安全性

                    if res is True:
                        return True
        return False

    def __DFS(self, board:List[List[str]], word:str, x:int, y:int, path_tracking: List[List[str]], signal):
        global break_signal
        break_signal = signal
        path_tracking = copy.deepcopy(path_tracking) #这里我们必须用deepcopy

        if len(word) == 1 and board[x][y] == word[0]:
            break_signal = True
            return True

        if break_signal: return True

        if board[x][y] == word[0]: # 若当前位置符合标准
            path_tracking[x][y] = True  # 更改tracking

            if x-1 >= 0 and (path_tracking[x - 1][y] == False):
                self.__DFS(board,word[1:],x-1,y,path_tracking, False)

            if break_signal: return True

            if x+1 < len(board) and (path_tracking[x + 1][y] == False):
                self.__DFS(board,word[1:],x+1,y,path_tracking, False)

            if break_signal: return True

            if y-1 >= 0 and (path_tracking[x][y-1] == False):
                self.__DFS(board, word[1:], x, y-1, path_tracking, False)

            if break_signal: return True

            if y+1 < len(board[0]) and path_tracking[x][y+1] == False:
                self.__DFS(board,word[1:],x,y+1,path_tracking, False)

            if break_signal: return True


foo = Solution()
print(foo.exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"))



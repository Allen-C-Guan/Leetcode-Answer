class Solution:
    def __init__(self):
        self.maxs = 0
    def cuttingRope(self, n: int) -> int:
        def DFS(begin, cur_res,rest_len:int):
            # 递归出口
            if rest_len == 0:self.maxs = max(cur_res,self.maxs)
            for next_len in range(begin, rest_len+1):
                DFS(next_len,cur_res*next_len, rest_len-next_len)
        for first_cut in range(1, int(n/2)+1):
            DFS(first_cut, first_cut, n-first_cut)
        return self.maxs



foo =Solution()
print(foo.cuttingRope(10))
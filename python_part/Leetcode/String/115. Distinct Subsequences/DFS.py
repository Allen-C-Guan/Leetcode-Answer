'''
超时！
其实对于回朔法，除非你已知长度很短 百个递归之内，不然就不要用回朔！！因为2**100 就很大了
回朔在问题size不确定的时候，永远是最后的选择

'''
class Solution:
    def __init__(self):
        self.cnt = 0
    def numDistinct(self, s: str, t: str) -> int:
        def DFS(begin:int, path:str):
            # 递归出口
            if begin > len(s) or len(path) > len(t):return  # 如果超过s的范围，或者比t还长，就不用找了
            # 记录成功的结论
            if path == t:
                self.cnt += 1
                return
            # 递归入口
            for cur in range(begin,len(s)):   # 回朔中最好的去重复的方法就是这里从begin开始，递归入口的时候，采用cur+1的方法避免重复
                if t.startswith(path + s[cur]): # 剪枝
                    DFS(cur+1, path+s[cur])
        DFS(0,"")
        return self.cnt

foo = Solution()
print(foo.numDistinct("babgbag","bag"))

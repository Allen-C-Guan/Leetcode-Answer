from typing import List
'''
这到题到精髓在于如何处理0，
0和其他值的不同在于，如果0出现在第一位上，那么0就已经独占一位了，没必要在往后继续扩展了。
例如：
0100, 这时候我们第一组的第一位选取了0，那么第一组就只有0这一种可能了， 没必要去看看01，010是不是符合标准了
如果我们第二组的第一位选的是1， 那么，第二组就有多种可能，1，10，100，我们仍要继续遍历
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def DFS(begin:int,path:List):
            # 递归出口
            if begin == len(s) and len(path) == 4:
                res.append(path.copy())  # 添加进去的path必须是copy
                return
            if len(path) >= 4:
                return
            #递归入口
            for cur in range(begin+1, min(begin+4,len(s)+1)):  #截取的部分不包含cur的
                # 剪枝
                if int(s[begin:cur]) < 256 and (len(s) - cur) <= 3 * (4-len(path)):  # 后面还够长，前面还在范围里,已经走过的总长度不超过3
                    path.append(s[begin:cur])
                    DFS(cur,path)
                    path.pop()
                    # 处理0， 0 如果是begin，那么只能独自一人作为head，没有01，因此循环在遍历到0之后就没有继续往下走的必要了
                    if s[begin:cur] == "0":break
        res = []
        DFS(0,[])
        for i in range(len(res)):
            res[i] = ".".join(res[i])
        return res


foo = Solution()
print(foo.restoreIpAddresses("01000"))
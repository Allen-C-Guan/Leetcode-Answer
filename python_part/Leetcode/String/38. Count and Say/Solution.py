class Solution:
    def countAndSay(self, n: int) -> str:
        cnt, pre = 2, "1"
        while cnt <= n:  # 递推计数
            i, cur = 0, ""
            # 查重模块
            while i < len(pre):
                runlength= 1
                while i + runlength < len(pre) and pre[i] == pre[i+runlength]:
                    runlength += 1
                cur += str(runlength) + str(pre[i])
                i += runlength
            pre = cur
            cnt += 1
        return pre


foo = Solution()
print(foo.countAndSay(1))

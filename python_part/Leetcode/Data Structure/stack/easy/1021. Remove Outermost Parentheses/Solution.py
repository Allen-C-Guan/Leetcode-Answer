'''
为何堆栈总和括号有不解之缘，就是因为结构特性。
即
保护现场。（当前结果入栈）
处理中断（处理当前问题）
还原现场（历史结果还原，与当前结果合并）

而且问题执行顺序都是先进的后出！！！！！！
'''

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack, res_list,cur,res = [],[],"",""
        for i in S:
            if i == "(": stack.append("(")
            else: stack.pop()
            cur += i
            if not stack:
                res_list.append(cur)
                cur = ""
        for j in res_list:
            res += j[1:-1]
        return res


foo = Solution()
foo.removeOuterParentheses("()(())(())")


'''

处理字符串有很多现成的好用的自带函数。
join
split("*")
count("*")
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")  # 这就一句话就完事了
        stack = []
        for i in path:
            if i == "..":
                if stack:stack.pop()
            elif i != "." and i: # i 非空 i不是"."
                stack.append(i)
        return "/" + "/".join(stack)

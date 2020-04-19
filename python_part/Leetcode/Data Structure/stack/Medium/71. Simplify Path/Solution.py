class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        size = len(path)
        while i < size:
            runlength = 1
            while i + runlength < size and path[i+runlength] != "/":
                runlength += 1
            if runlength > 1: # 这里面有内容,并不是只有两个//
                content = path[i + 1:i + runlength]
                if content == "..":# stack里有东西，而且需要退回一步。
                    if stack:
                        stack.pop()
                elif content != ".":
                    stack.append(content)
            i += runlength
        return "/"+"/".join(stack)

foo = Solution()
print(foo.simplifyPath("/../"))









from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        pattern, dist, res = Counter(words), len(words[0]), []
        for begin in range(len(s)-len(words) * dist+1):
            cur_list = [s[begin+cnt*dist:begin+(cnt+1)*dist] for cnt in range(len(words))]
            if Counter(cur_list) == pattern: res.append(begin)
        return res

foo = Solution()
print(foo.findSubstring("barfoothefoobarman", ["foo","bar"]))




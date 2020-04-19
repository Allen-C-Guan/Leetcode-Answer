from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        pattern = Counter(words)
        dist = len(words[0])
        res = []
        for begin in range(len(s)-len(words) * dist+1):
            cur_dic = {}  # 建立一个新字典
            for cnt in range(len(words)): # 最多循环 len(words) 不然肯定是有重复段
                cur_word = s[begin+cnt*dist:begin+(cnt+1)*dist]
                if cur_word in pattern:  # 如果当前段在pattern中
                    cur_dic[cur_word] = cur_dic.get(cur_word, 0) + 1
                else: break # 只要有非法字符段插入，就不用在循环了
            if cur_dic == pattern: res.append(begin)
        return res


foo = Solution()
print(foo.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))





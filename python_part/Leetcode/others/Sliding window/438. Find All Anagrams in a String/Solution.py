from typing import List
from collections import Counter
'''
Counter(List)，return的是list得到的统计数据，key是项目， 出现的次数是value

很可惜，这个方法效率仍然不够。 特别是如果p的长度太长，这导致整个算法效率极低。
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len, parttern_dic, res = len(p), Counter(p), []

        for i in range(len(s)):
            cur_s = s[i:i+p_len]
            if Counter(cur_s) == parttern_dic: res.append(i)
        return res



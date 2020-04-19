'''
dict的题，解决的最多的就是和重复和查找有关的题。
如果问题在解决的过程中有重复的中间过程，可以存下来。
如果问题需要不停的查找，那么也要用hash table

'''
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cheet_dic,res = {}, set()
        for i in range(len(s)-9):
            cheet_dic[s[i:i+10]] = cheet_dic.get(s[i:i+10], 0)+1
            if cheet_dic[s[i:i+10]] > 1:
                res.add(s[i:i+10])
        return list(res)

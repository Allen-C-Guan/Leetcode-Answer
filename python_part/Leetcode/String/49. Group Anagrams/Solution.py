from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cheet_dic = {}
        for s in strs:
            s_sort = "".join(sorted(s))   # sorted可以直接sort string返回的是list
            if s_sort in cheet_dic:
                cheet_dic[s_sort].append(s)
            else:
                cheet_dic[s_sort] = [s]
        res = []
        for val in cheet_dic.values():  # .values()  .items(), .keys() 才可遍历呢。
            res.append(val)
        return res

foo = Solution()
print(foo.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))


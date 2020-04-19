from typing import List
'''
time: O(nlogn)
memo: O(n)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cheet_dic = {}
        for n in nums:
            if n in cheet_dic: cheet_dic[n] += 1
            else: cheet_dic[n] = 1
        sort = sorted(cheet_dic.items(), key= lambda x:x[1], reverse=True)
                                            # 这一步我们用sorted，复杂度是O(nlogn) 如果用min heap，则为O(nlogk)
        res = []
        for key, value in sort[:k]:
            res.append(key)
        return res

foo = Solution()
print(foo.topKFrequent([1,1,1,2,2,3],2))
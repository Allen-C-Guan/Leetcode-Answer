from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thresh = int(len(nums)/2 + 1)
        cheet_dict = set()
        for i in nums:
            if i in cheet_dict: continue
            else:
                temp = nums.count(i)
                if temp >= thresh:
                    return i
                else:
                    cheet_dict.add(i)




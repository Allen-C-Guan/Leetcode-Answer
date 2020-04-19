'''
这是O(n^3)的算法，效率很低
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for left in range(len(s)):
            helper_set = set()
            for right in range(left,len(s)):
                if s[right] in helper_set:
                    break
                else:
                    helper_set.add(s[right])
            res = max(res, len(helper_set))
        return res
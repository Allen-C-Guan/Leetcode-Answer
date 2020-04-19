from typing import List
'''
时间复杂度高，看起来也用不了DP，因为DP类似的问题也需要至少两个for来建表。
当算法给不了过多帮助的时候，最先想到的应该是数据结构！
而降低复杂度最常见的避免重复的方法是利用dict来记录数据！

如何定义状态过程，成为使用dict最关键的问题。
对于这个问题，我们可以定义sum为key，出现的次数为value。这样我们可以利用集合的概念，截取一部分连续序列的值。
这样我们从前往后遍历，遍历到任何一个sum的时候，我们检查sum-target是否已经出现在前面，如果出现过，就说明前面必有一段连续子序列的和==k，
且该子序列以当前元素为截止。

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cheet_sheet, sums, cnt = {0: 1}, 0, 0
        for item in nums:
            sums += item
            if sums - k in cheet_sheet:
                cnt += cheet_sheet[sums-k]
            cheet_sheet[sums] = cheet_sheet.get(sums, 0)+1
        return cnt


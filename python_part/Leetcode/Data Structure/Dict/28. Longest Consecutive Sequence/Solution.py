'''
第二种方法可以实现的理论基础在于，我们永远只会用到端点处的value，因此即使中间的数字，在dp的过程中，并没有及时更新，也不再正确，
但是没关系，反正用不到了。

而为何只用端点值是因为连续导致的。 连续就会导致中间的值永远不可能再被用到，因为可能用到中间值的只能是他的邻居， 而他的邻居已经被放在了区间中了。

至于为何不需要区分是左端点还是右端点，而是只存放以当前点为端点的连续序列目前的长度，是因为map中存放的值，一定是连续序列已经遍历过
的部分组成的。而若遍历过的部分组成的部分为左边，那说明右边一定没遍历过，那如果你这时候需要该端点了，一定是因为你碰到了端点右边的值，
那么左边的长度 + 右边的长度就一定是正确的，因此一定可以保证衔接的方向的正确性。

其实这本质上是数学集合的问题，每个数存放的都是以该点为端点的已经遍历过的部分，那么没遍历过的一定处在该端点的另一侧。

'''

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic, max_len = {}, 0
        for item in nums:
            if item not in dic:
                left = dic.get(item-1,0)
                right = dic.get(item+1,0)
                cur_len = dic.get(item-1,0) + dic.get(item+1,0) + 1  # 获取当前的序列长度
                max_len = max(cur_len, max_len)
                dic[item] = 1                                      # 为了用来查重，第一次进来一定要加进来。赋值是多少都行，不重要。
                dic[item-left] = dic[item+right] = cur_len         # 更新端点的值
        return max_len

foo = Solution()
foo.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])
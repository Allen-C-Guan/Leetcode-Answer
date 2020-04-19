'''
就这两个O(n^2) 还超时！！！
该题思路就是通过分类讨论，拆分集合，来避免重复的情况的发生。
因为要想用两个循环，就要检查第三个量是否在list中，而这个检查的过程中，就会导致可能查到自身。
为了避免检查是否第三个量可能会是自身的情况，我们只要分类讨论，让第三个量不在自己的集合中，就永远不会发生重复的情况
'''


class Solution:
    def threeSum(self, nums):

        nums = sorted(nums)
        #sort很重要，sort可以让完全相同的组合具有同样的顺序，这样在检查是否已经存在的时候，就很容易被查出来了

        neg_list = []
        pos_list = []
        zero_list = []
        res = []

        for n in nums:
            if n < 0:
                neg_list.append(n)
            elif n > 0:
                pos_list.append(n)
            else:
                zero_list.append(n)

        neg_set = set(neg_list)
        pos_set = set(pos_list)
        zero_cnt = len(zero_list)

        # two pos with one neg
        for i in range(len(pos_list)):
            for j in range(i+1, len(pos_list)):
                if -(pos_list[i]+pos_list[j]) in neg_set:
                    temp = [pos_list[i], pos_list[j], -(pos_list[i]+pos_list[j])]
                    if temp not in res:
                        res.append(temp)

        # two neg with one pos
        for i in range(len(neg_list)):
            for j in range(i + 1, len(neg_list)):
                if -(neg_list[i] + neg_list[j]) in pos_set:
                    temp = [neg_list[i], neg_list[j], -(neg_list[i] + neg_list[j])]
                    if temp not in res:
                        res.append(temp)
        # one pos one neg one zero
        if zero_cnt != 0:
            for i in pos_set:
                if -i in neg_set:
                    res.append([i,-i,0])

        # triple zero
        if zero_cnt >= 3:
            res.append([0,0,0])

        return res

foo = Solution()
print(foo.threeSum([]))


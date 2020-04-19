'''
Solution 2 给我提供了一个思路，那就是将可能的答案计算出来，而后去寻找。

1. 一说到寻找， 自然就会想到dict在寻找中的作用，因此，我们可以简单的将list建立成dict，而后在list中循环，在dict中寻找答案即可

2. enum类型的数据可以帮助dict的建表。
        1).enum的数据是可以含有key和value两个部分组成，有点类似dict
        2). enumerate()函数可以自动的将list变成enum，且其key是index，而value是list中的内容。
    因此 通过enum类型的数据，可以将list很快转化成为dict的数据，而enumerate() 函数更是自动将index和value都分开存放
3. 之所以dict可以直接避免了因为重复项问题而导致的缺少答案，例如 [3, 3]  6，是因为，我们遍历的时候是从list前到后的，而相同元素在dict中的值一定是list后面的那一个
因此我们一定不会错过这样的答案
'''
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[value] = index

        for i in range(len(nums)):
            complement=target - nums[i]
            if complement in hashmap and i != hashmap[complement]:  #根据第三条，这里对比的一定是list从前往后的index与hashtable中值（若值相同，则为后面的元素的index）
                return i, hashmap[complement]



print(Solution.twoSum("allen",[3,3], 6))


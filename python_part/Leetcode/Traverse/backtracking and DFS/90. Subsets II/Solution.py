from typing import List
'''
看似简单的防止重复的条件竟然是很多其他部分的配合造成的：
1. 前提：必须是sorted array。因为只有sorted array才能用相邻的方法来判定是否是重复的
2. 记录过程： 因为是子集问题，我们要记录全部的过程，每个过程都是一个子集！！
3. cur > begin 一定在前，nums[cur] = nums[cur-1]一定在后！！

注意：
1. for循环是一个可以自行开头的结构。
2. cur > begin 要写在前面。不然会报错
3. 该判定条件判定的是非法情况，因此后面要跟着的是continuous
4. 递归的入口处，一定是cur+1，而不是begin+1
5. 回朔清理要紧跟在递归之后，有几个递归，就有几个清理才对。

再次强调回朔的结构
if 出口   
    记录结果
    return 

if 剪枝条件  （可以没有）
    剪枝操作
    return 

for （所有下一等级的备选方案）：
    if: 继续剪枝的条件  #可以没有，但通常包括，避免重复，提前终止（已经知道继续下去没有意义）等条件
        
        记录当前位置
        递归（cur+1)
        回朔清理
    
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        self.__DFS(sorted(nums), 0, [], res)  # 排序是后面防止重复的条件的前提！！！
        return res

    def __DFS(self, nums,begin,path,res):
        path = path.copy()
        # 回朔出口
        if begin > len(nums)-1:
            return
        for cur in range(begin, len(nums)): #这个for循环本来就可以自行开头
            if cur > begin and nums[cur-1] == nums[cur]: #这个防止重复的条件是不合法判定，又是第二个以后，又重复就continue，保证第一个for中第一个无论如何要进来。
                continue
            path.append(nums[cur])          # 记录当前节点
            res.append(path.copy())         # 因为是子集，沿途的都要记录！！！！！这和避免重复的条件是成对出现的。要用copy否则会导致privacy leak
            self.__DFS(nums,cur+1,path,res)   # 这里是cur+1！！！！ ！！！！！！！！！！！！！！！！
            path.pop()                      # pop要紧跟在递归之后。每一次递归结束都要回朔清理。这是因为一个for循环公用一个path

foo = Solution()
print(foo.subsetsWithDup([4,4,4,1,4]))
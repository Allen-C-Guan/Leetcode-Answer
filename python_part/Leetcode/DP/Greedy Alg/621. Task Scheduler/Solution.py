from typing import List
'''
dict的用法：
dict.get(key,default_val) 获取key的value，如果没有返回default_val


(任务 A 出现的次数 - 1) * (n + 1) + (出现次数为最多次数的任务个数)
特殊情况：len(tasks)和我们算出来的还要取最大值。

'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        dupli_dict = {}
        for i in tasks:
            dupli_dict[i] = dupli_dict.get(i, 0) + 1

        dupli_list = sorted(dupli_dict.items(), key = lambda x:-x[1])

        max_times_classes = 0
        for i in dupli_list:
            if i[1] == dupli_list[0][1]: max_times_classes += 1

        return  max((dupli_list[0][1]-1)*(n+1) + max_times_classes,len(tasks))




foo = Solution()
print(foo.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))


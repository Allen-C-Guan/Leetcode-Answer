'''

如果用回朔就没这么多逼事了

这道题循环嵌套有点多，思路有点乱。
为了减少重复计算量，我们选择遍历的顺序为 以某个值作为开头的全部subset。并记录同一个head，同一个长度全部subset，因此长度加一的时候，我们可以直接在上一组
subset的基础上直接加一个值，就成了新的长度增加1的subset组了。

那么第一层循环就是head的从左到右的循环

第二层循环是subset的长度：subset的长度必然要从1到结尾的长度（size - head)：因此一组subset都具有相同的head和长度。

第三层 则是将上一组subset一一拿出来，在其后面从前往后加一个元素。但为了避免重复，我们只能选择处在结尾元素后面的元素中挑选。
        实现结尾元素之后的方法就是先找到结尾元素的位置，用while循环把该位置之后的元素都加进去。

'''

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = [[]]
        for head in range(size):
            res.append([nums[head]])
            pre = [[nums[head]]]
            for set_length in range(size-head):
                new_list = []  # 同一长度下的所有list的可能
                for pre_one in pre:
                    pre_tail = nums.index(pre_one[-1])
                    new = pre_tail+1
                    while new < size:
                        new_list.append(pre_one+[nums[new]])
                        new += 1
                if len(new_list) != 0:
                    res = res + new_list
                    pre = new_list
        return res
                    
foo = Solution()
print(foo.subsets([1,2,3]))




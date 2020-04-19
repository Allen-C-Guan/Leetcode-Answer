'''
上一个方法的复杂度是O(n^2) 如果使用双指针 只要遍历一遍数组即可。
思路如下：
设置两个指针， i表示遍历指针，j表示将要被覆盖的指针。当i遇到了需要前移的元素，就将当前位置的元素，向j所指向的位置覆盖。

双指针的问题：
我们不但要利用指针i来判定，也要利用j啊！！ 对于双指针的问题，总是忘记一个指针的作用！！

判定是否可以加入的条件为：
    nums[i] 是否等于 nums[j-2]

解释如下：
 我们要知道 j 之前的list表示的已经排好序的内容，既然要避免重复两次以上，只要判定排好的倒数第二个和当前的是否相同就好了。
 这是因为！

    我们只在乎没排好的（与i有关）和排好的（与j有关）之间的关系就行了，我们不用在乎两者之间的废物内容！！！！！

我之前的错误在于只关注了i前后的关系。


'''

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        j = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1
        return j

foo = Solution()
foo.removeDuplicates(
[1,1,1,2,2,2,3,3])




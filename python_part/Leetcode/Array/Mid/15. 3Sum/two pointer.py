'''
数组里面： 排序+双指针的方法真的是爸爸级别的方法。
因为一旦排序发生，我们可以根据目前得到的结果与期望的结果之间进行对比，根据大小关系，定向的移动双指针。
也正是因为定向移动指针，让我们舍弃了很多不必要的遍历，从而节省时间。

该思路的方法通常为：
1. 利用数学特性，通过结果与期望的关系，来让指针定向变换。

这里和dp的思想完全不同，这里我们只是缩小了candidates的范围，并没有说这样选出来的都是符合条件的。因此我们通常缩减了范围以后，还是需要继续判定的。

这里我们需要论证，为什么pivot只要不重复，那么得到的结论就一定是即不落下也不重复的：



证明不重复：
若我们在选择pivot的时候，不选择重复的。则有如下结论

首先pivot是从前向后遍历的，而另两个元素也只能从其右边挑选。

那么所有挑选出来的组合必定是： pivot（必包含） + 其之右的两个元素
            上式组合中还有个特点： 叫必不包含pivot之前的元素。

但我们还需要保证 "其之右的两个元素" 组合没有重复，就可以保证唯一性

倘若pivot不选择重复的元素，且设 pre-pivot表示当前pivot之前的pivot。则pre-pivot选出的元素可以表示为：
            pre-pivot（必包含） + 其之右的两个元素
            而pre-pivot必不在组合： pivot（必包含） + 其之右的两个元素 之中。
            因为该组合必不包含pivot之前的元素，而pre-pivot就是pivot之前的元素，且还必在其中。因此两个集合一定并无交集


证明不落下：
若所有元素各不相同。那么 每个元素分别成为一次pivot，必然可以遍历所有可能的可能组合。（为什么说是可能的可能性，因为我们没有遍历全部，我们是定向移动指针）
因为在单独一个pivot的循环中，我们算是遍历了所有在pivot必存在的条件下，且不包含之前已经计算过的部分 的全部可能性。

但是别忘了，我们还跳过了重复的pivot，当重复的pivot出现时，我们选择了视而不见。会不会在这种情况下落下某个部分呢？

该问题可以分成三类来讨论：
例如 list[a, a ,a , b, c, d]
当pivot是第一个a的时候,组合可以分成如下3种

1. a + a + others
2. a + a + a
3. a + a + others
这里other指的是集合[b, c, d]

当pivot是第二个a的是，如果继续遍历，组合有如下两种
1. a + a +others
2. a+ others

当是第三个a的时候，如果继续遍历，组合只有一种可能：
1. a + others

我们发现，如上三种情况，其实pivot是第一个a的时候，就已经全部包括了，第二个a和第三个a完全是没有增加任何可能性。
因此我么直接跳过并不会丧失任何可能性。



综上所述，我们可以得出一个重要的按顺序但遍历list的思想：
这只是一个升级版的list里面选两个元素的方法。即每个后手都在先手的后面选，就不会造成重复。换句话说后手一定不要碰先手之前的部分。
但是一定要注意pivot重复的情况。pivot一旦重复就直接跳过

如果并不是按顺序遍历，例如双指针，就要保证相同元素就要跳过。


如何既不重复也不跳过，我们只要让多个相同的东西，只有其中一个进入到循环中，其他的不进入。就行
'''


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []

        for pivot in range(len(nums)-2):
            if nums[pivot] > 0:  #提前结束，如果pivot都比0大，那就另外两个也大于0，因为只能在其右选择。
                break
            if pivot > 0 and nums[pivot-1] == nums[pivot]:  #pivot一定不能选择重复了, 为了避免indexOutOfRange,要在前面加上条件。后面就不会被执行了
                continue
            left = pivot+1
            right = len(nums)-1
            while left < right:
                temp = nums[left] + nums[right] + nums[pivot]
                if temp == 0:
                    res.append([nums[pivot], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    '''
                    这里我们用while循环向前推，直到找到不同为止。
                    我们先减去或加上之后，再进入循环的目的是为了防止indexoutofrange的发生。
                    
                    '''
                    while nums[right] == nums[right+1] and right > left: right -= 1
                    while nums[left] == nums[left-1] and right > left: left += 1
                elif temp > 0:
                    right -= 1
                    while nums[right] == nums[right+1] and right > left: right -= 1

                else:
                    left += 1
                    while nums[left] == nums[left-1] and right > left: left += 1


        return res

foo=Solution()
print(foo.threeSum([-1,0,1,2,-1,-4]))
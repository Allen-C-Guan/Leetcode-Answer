'''
这道题的思路：
由于要求以log(n)的级别去解决问题，且原序列是排好序的，于是我们就用二分法。

可是对两个数组如何采用二分法呢？右如何比较来确定当前的大小呢？
我们发现符合条件的p1和p2必须满足两个条件：
1. p1 + p2 等于两条数组的长度和的一半
2. 必须有 p1 和 p2 均大于两者之前的所有元素


关联指针法：
因为 p1+p1 = int((n+m+1)/2)的数量关系，我们发现p1和p2看似是两个指针，但却只有一个自由度。因此我们可以只对一个指针做二分，另一个指针自然会随之而动

如何确定大小：
如果我们用关联指针方法，那么条件1自然已经满足。我们只需要用二分来判定条件2即可。
判定的方法就是：
若p1 - 1 > p2 说明 p1仍然太大，要左移
若p2 -1 > p1 说明p1 不够大，要右移

边界的处理：
由于p1-1 和 p2-1的出现，我们需要考虑边界问题。
可是这里，一旦p1到达了边界(0 或者 m）。也就不需要找了啊！！因此此时说明已经找到了。说明p1一个没用。或者p1已经全用上了。无论是哪个。都已经找到了啊。
因为p1固定了。p2也就随之而定了。


收尾处理：
我们仍然要考虑序列的奇偶长度给出不同的答案。
并且你只是找到了边界，边界就是p1 和 p2 之前为边界，那么边界后符合条件的是哪个？ 就要分析了。要取左边最大的，右边最小的。


'''


from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        # 保证nums1 永远是短的，其长度为m， 则nums2永远是长的， 长度为n
        # i = 0  # nums1的pointer
        target = int((m+n+1)/2)
                    # 对于奇偶数不定的情况，int((m+n)/2)表示的是：奇数序列中的中间值，偶数序列中的中间两个值的左边的那个。
        left = 0
        right = m  # right 必须是m开始，如果是m-1开始，那么nums[m-1]有可能被循环不到。
        '''
        寻找成功的终点为：
        1. 符合条件 nums1[p2] > nums[p1-1] and nums[p1] > nums[p2-1] 的时候
        2. 当p1 走到头的时候：
            当p1走到了0处 说明nums1 很可能一个没用或者用了一个
            当p1走到了m处。  说明nums1即使全用上了也不够填补一半的长度。
            
            这两种情况下，中位数的值已经确定下来了。
            
        那么什么时候才需要继续找呢？
        需要同时满足如下条件：
        1. p1 没有走到头
        2. 依然没有找到符合条件的点
        '''

        while left <= right:
            p1 = int((left + right)/2)  # mid of nums1
            p2 = target - p1
            '''
            这里由于我们的设定是 p1+p2 = int((n+m)/2) 因此 若有 p1>0, 必有p2 < n 同理若有 p1<m 则p2>0必成立
            换句话说，只要有一个不到头（尾）！另一个也肯定没法到尾（头） 。
            '''
            if p1 < m and nums1[p1] < nums2[p2-1]: # p1 (中点）不够大
                left = p1+1
            elif p1 > 0 and nums2[p2] < nums1[p1-1]: # p1 （中点）太大了
                right = p1-1
            else:   # 这时候就可以了，不用继续找了
                '''
                这个时候就要看看当前的落点和m+n的奇偶性来确定了。
                如果你定义的是target = int(m+n+1)/2 表示的是奇数的中点，或者偶数的中间两个的左边的一个。
                我们把奇数中间的和偶数中间的左边的一个叫做 max_of_left 
                把偶数中间的右边的叫做min_of_right
                于是 根据跳出的3种情况来选择最终的位置。
                1. P1一个没用：是因为nums2[target-1] < nums1[0] 也就是说这时候nums1[0]仍然太大了。
                    这时候自然就应该是nums2[target-1]就是对的值
                2. P2一个没用：是因为nums1[target-1] < nums2[0] 也就是说nums2[0]还是太大了
                3. 正常退出的:
                    1. p1已经超过了m-1范围,这说明p1都用上也不够 
                    2. p1和p2都停留在某个特定都位置上。
                
                退出以后，我们要在p1和p2停留处，挑选，挑选合适的位置
                '''

                if p1 == 0:
                    max_of_left = nums2[target-1]
                elif p2 == 0:
                    max_of_left = nums1[target-1]
                else:
                    max_of_left = max(nums1[p1-1],nums2[p2-1])  #中心处

                if (m+n) % 2:
                    return max_of_left

                if p1 == m:
                    min_of_right = nums2[p2]
                elif p2 == n:
                     min_of_right = nums1[p1]
                else:
                    min_of_right = min(nums1[p1], nums2[p2])

                return (max_of_left + min_of_right)/2



foo = Solution()
print(foo.findMedianSortedArrays([3,4,5],
[7,8]))











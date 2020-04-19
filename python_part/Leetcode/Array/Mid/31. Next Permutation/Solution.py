'''
1. 找到结尾部分全部逆序的部分的前一位。
    例如 1，3，7，4，2。这里面 742 是倒序，那么此时前一位就是3
2. 在结尾倒序部分选出所有大于该值中的最小的一个，与该位互换，于此同时还保留了后面的序列还是倒序。
    例如，上面的例子，可以找到4，因为4是比3大的数字中最小的，互换，得到 1,4, 7, 3,2 ,那么 732仍然保持了倒序的结构
3. 把互换后的序列正向排列得到：
    1, 4, 2, 3 , 7  排序完成

其中第一条是性质。
第二条是因为，互换的元素一定是最接近被换元素的大值，因此互换不会扰乱后面倒序的顺序。

但这里有个问题是in-place 这让排序变得很麻烦。不过好在后面还是倒序，因此倒序也算有序，变正序简单点。中心对称互换即可
'''




class Solution:
    def nextPermutation(self, nums) -> None:
        size = len(nums)

        head = size-1 # 若head = size - 1表示序列整个都是倒序的（最大值）
        for i in range(size-2, -1, -1):
            if nums[i] < nums[i+1]:
                head = i
                break
        # 当最大序列发生的时候
        if head == size-1:
            self.swap(nums, 0, size-1)
            return

        for new_head in range(head+1, size): #这个前提是head不再最后一位上(即最大值）。
            if nums[new_head] <= nums[head]:#这有个问题在于如果head已经是最小的值怎么办
                new_head -= 1     #如果找到了，就减1，找不到就不减1
                break
        nums[head], nums[new_head] = nums[new_head], nums[head]

        #互换的终点(要包含该终点）应为 int( (start+end)/2 ) 那么得到的结果是如果区间是奇数个，那么最后是中间自己根自己互换，如果是偶数个，就正常互换，不多不少
        #这是因为对换中心为 (start+end)/2，这个中心在区间是奇数的时候，和中间那位重合，若是偶数区间，就是中间两个的中间
        nums = self.swap(nums, head+1, size-1)

    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


foo = Solution()
foo.nextPermutation([1,5,1])







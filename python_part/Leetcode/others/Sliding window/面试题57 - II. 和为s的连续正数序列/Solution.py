from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 1
        window_sum = 0
        res = []
        while left <= int(target/2) and right <= int(target/2)+1:
            # 移动右指针： 右指针找可行域
            while window_sum < target:
                window_sum += right
                right += 1
            # 移动左指针：在可行域中寻找可行解
            if window_sum > target:
                while window_sum > target:
                    window_sum -= left
                    left += 1
            # 走到这的，不是等于就是小于
            # 这里要更新可行域，新的可行域只是可行解left向右一步
            if window_sum == target:
                res.append(list(range(left,right)))
                window_sum -= left
                left += 1
        return res
foo = Solution()
print(foo.findContinuousSequence(15))
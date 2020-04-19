from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cnt, cur, is_pre_increase = 1,  0, None
        while cur < len(nums)-1:
            increase_cnt = 1
            while increase_cnt + cur < len(nums) and nums[increase_cnt+cur-1] < nums[increase_cnt+cur]:
                increase_cnt += 1
            if increase_cnt > 1:
                cur += increase_cnt-1

                if not is_pre_increase:
                    cnt += 1
                    is_pre_increase = True

            # cur 应该指向极值点
            decrease_cnt = 1
            while cur + decrease_cnt < len(nums) and nums[cur+decrease_cnt-1] > nums[cur+decrease_cnt]:
                decrease_cnt += 1
            if decrease_cnt > 1:
                cur += decrease_cnt-1
                # 判定上一段单调区间
                if is_pre_increase == None or is_pre_increase:
                    cnt += 1
                    is_pre_increase = False

            # 相同的时候 ie. 5 5
            if increase_cnt == decrease_cnt == 1:
                cur += 1

        return cnt
foo = Solution()
print(foo.wiggleMaxLength([1,2,2,3,3]))

'''
滑动窗口法:
字典能遍历的是.items .keys 不是dict本身

这里不需要更新left和right因为left和right会while循环结束的时候，自行各向右移动一位。且在left的循环中，while会把window最左端边符合条件
的字符串删除
'''

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, pattern, res, cur = 0, 0, Counter(t), "", {}
        while right < len(s):
            # right 在向右扩展，扩展到比需求量大的时候
            while not self.isLarger(pattern, cur) and right < len(s): # 既没有到头，也没有找到可行域
                c = s[right]
                if c in pattern:  # 当前元素是当前之一
                    cur[c] = cur.get(c, 0) + 1
                right += 1

            # 如果已经找不到可行域了，就返回把
            if not self.isLarger(pattern, cur): return res

            # left向右移动
            while self.isLarger(pattern, cur):
                if s[left] in pattern:
                    cur[s[left]] -= 1
                left += 1

            # 找到了极小值，进行判定
            temp = s[left-1:right]
            if len(res) == 0 or len(temp) < len(res):
                res = temp

        return res

    def isLarger(self, pattern: dict, cur: dict):
        for key, value in pattern.items():
            if value > cur.get(key, 0): return False
        return True


foo = Solution()
print(foo.minWindow("ADOBECODEBANC", "ABC"))



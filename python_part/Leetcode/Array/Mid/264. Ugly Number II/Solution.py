'''
超时
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hist_set = {1, 2, 3, 4, 5}
        if n < 7: return n
        cnt = 6
        while len(hist_set) < n:
            if cnt/2 in hist_set or cnt/3 in hist_set or cnt/5 in hist_set:
                hist_set.add(cnt)
            cnt += 1
        return cnt - 1
foo = Solution()
print(foo.nthUglyNumber(7))
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def isValid(x: int, y: int):
            bit_sum = 0
            while x != 0:
                bit_sum += x % 10
                x = int(x / 10)
            while y != 0:
                bit_sum += y % 10
                y = int(y / 10)
            return bit_sum <= k

        def infect(x: int, y: int):
            # 回朔出口
            # 超出边界
            if x < 0 or x > m - 1 or y < 0 or y > n - 1: return 0
            # 超出k约定距离
            if not isValid(x, y) or (x, y) in footprint: return 0
            # 记录当前信息
            footprint.add((x, y))
            return infect(x + 1, y) + infect(x, y - 1) + infect(x - 1, y) + infect(x, y + 1) + 1
        footprint = set()  # 我们在回朔的时候，不但要知道怎么走出去，还要记录足迹，为的是防止重复。

        return infect(0, 0)


foo = Solution()
print(foo.movingCount(2, 3, 1))

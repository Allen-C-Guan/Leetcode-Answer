'''
与brute force的方法类似，但brute force从两端向中间，这就很蠢，因为两端需要两个for循环的嵌套来实现。

回文，中心对称的特点，我们自然可以从中间扩展开来，只遍历中心位置。 这只需要一个for循环

但该方法最大的问题是：奇数，偶数的回文并不同，这让我们的判定变得很复杂。

但是我们可以将两种情况合二为一！
1。我们在设计判定是否回文的function中，我们同样给出两个指针，并让两个指针从中间向两边扩展。
2。传参我们可以分两种情况来传入：
        若pivot是i，则：
        1） pointer1, pointer2 = i, i   这样扩展出来的是奇数序列
        2) pointer1, pointer2 = i, i+1  这样扩展出来的是偶数序列



边界条件：
对于边界条件：
用一个size为5的试一下就知道了

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s

        max_len = 1
        res = s[0]
        for i in range(1, length):
            res1, len1 = self.centreSpread(s, i, i)
            res2, len2 = self.centreSpread(s, i - 1, i)

            temp_max_len = max(len1, len2)
            if temp_max_len > max_len:
                max_len = temp_max_len
                if len2 > len1:
                    res = res2
                else:
                    res = res1
        return res

    def centreSpread(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:    #  可以把条件写在这里！！！
            left -= 1
            right += 1
        return s[left + 1:right], right - left - 1


foo = Solution()
print(foo.longestPalindrome("babad"))

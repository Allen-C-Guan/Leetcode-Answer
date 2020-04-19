
'''
小学奥数，没啥可讲的。这要不会回去种地把
'''

class Solution:
    def romanToInt(self, s: str) -> int:

        if len(s) == 0:
            return 0

        R2I_map = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M":1000}

        res = R2I_map[s[0]]
        for i in range(1, len(s)):
            if R2I_map[s[i]] <= R2I_map[s[i-1]]:
                res += R2I_map[s[i]]

            else:
                res = res - R2I_map[s[i-1]]*2 + R2I_map[s[i]]

        return res






foo = Solution()
print(foo.romanToInt("MCMXCIV"))



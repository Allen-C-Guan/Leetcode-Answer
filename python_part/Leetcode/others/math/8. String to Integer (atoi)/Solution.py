'''
这垃圾题，我吐了！！

这题就是脑筋急转弯
其实这题用python正则表达式就行，然而我懒得想了。

只要知道这三个公式就行了。

1. "Symbol".join(list1)就是把list中每个元素以symbol相连
2. list(str1) 就是把string按char来拆分
3. string1.split("symbol") 把string按symbol来拆分， symbol 默认为空格


'''

class Solution:
    def myAtoi(self, str: str) -> int:
        str = list(str.strip())  # 只删除两头的space
        neg = False
        '''
        符号只能出现在最开始，出现就记下然后删除就行来
        '''
        if not len(str):
            return 0
        if str[0] == "-":
            neg = True
            del str[0]
        elif str[0] == "+":
            del str[0]

        size = len(str)
        map = {"1": 1,
               "2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "0": 0}
        res = []
        for i in range(size):
            if str[i] in map:
                res.append(str[i])
            else:
                break

        res = "".join(res)
        if not len(res):
            return 0

        res = -int(res) if neg else int(res)

        if -2 ** 31 > res:
            return -2 ** 31
        elif res > 2 ** 31 - 1:
            return 2 ** 31-1
        else:
            return res


foo = Solution()
print(foo.myAtoi("2147483648"))
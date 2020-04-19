# 递归解法

'''
在该方法中，我们采用 "in"来完成对成员变量对搜索，每次while循环会找到最少一个可以相消的括号对，然后消去后重新检测，直到全部消去为止。

若消到最后，没有任何剩余，则说明是可行的，否则则为不行。
'''


class Solution:
    def isValid(self, s: str) -> bool:  # 冒号指明变量类型，箭头规定返回类型
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")  # 函数连着写是把前面的计算结果当成一个str继续调用函数
        return s == ''

        '''
        bytes.replace(old, new[, count])
        bytearray.replace(old, new[, count])
        返回序列的副本，其中出现的所有子序列 old 都将被替换为 new。 如果给出了可选参数 count，则只替换前 count 次出现。
        '''


foo = Solution() #带括号表示实例化，不带括号是赋值
                #万物皆为obj，如果是foo = Solution，则foo也是一个class。
print(foo.isValid("{[()]}"))



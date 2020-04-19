
'''
本题中使用滑动窗口的方法来减少重复的计算。
滑动窗口方法适用于很多的  无序子集 的问题！
该方法的实现是通过两个指针来模拟窗口左右的两个边，而后通过两个指针的异步向右滑动，来实现窗口的放大，缩小，移动。
而我们只要通过对窗口内的内容进行统计，即可以判定窗口内的内容是否符合条件。

那么如何移动左右指针呢？
通常情况下：
右指针负责将窗口拉到可行域中（右端点负责扩大窗口）
左指针负责在可行域中寻找可行解。（左端点负责缩小窗口）

在这个特定的题中：
1. 右端点选择可行域。窗口内不得有任何不再p中的字符，这就意味着，right当发现非法字符的时候，就已经不是可行解了，可行域就要发生变化
    这时候window马上越过当前字符，移动到当前右端点的右边，且长度缩减为0（left = right = right + 1)

2. 左端点判定负责判定当前可行域窗口是否是可行解：
    可行解的要求： 1. 长度 == len(p) 
                 2. cur == pattern  
    两个关系是同时满足的才是可行解。
    
    左端点何时缩小窗口：
        1. 当window窗口长度到达len(p)的时候，左端点就一定开始要缩短了。因为window的长度是没有必要超过len(p)的。
        2. 当window还不够长的时候，（因为window里的内容一定是p中存在的），因此我可以再观望观望。等着right继续扩大window长度
        综合上，即只要window够长了，就要缩短，不管当前window内的是不是可行解

'''
from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = right = 0
        pattern, cur, res = Counter(p), {}, []
        while right < len(s):
            c = s[right]
            if c in pattern:  # 如果 right在pattern里面就把当前right指的内容加进来
                cur[c] = cur.get(c, 0)+1
                if right - left + 1 == len(p):
                    if cur == pattern: res.append(left)
                    cur[s[left]] -= 1
                    left += 1
                right += 1
            else:
                right = left = right + 1
                cur.clear()
        return res


foo = Solution()
print(foo.findAnagrams("cbaebabacd" , "abc"))
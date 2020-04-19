'''
题中规定了扰乱的方法，不能随便扰乱。
    "挑选任何一个非叶节点，然后交换它的两个子节点。"

因此我这个方法并不行。
'''




class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        s1 = [i for i in s1].sort()
        s2 = [i for i in s2].sort()

        return s1 == s2

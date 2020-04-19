
'''
bin()得到是str。str下面有count("char")的功能。
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")



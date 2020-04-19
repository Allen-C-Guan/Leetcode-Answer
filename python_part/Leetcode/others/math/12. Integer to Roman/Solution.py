'''
这题在侮辱的我的智商么？？？这题还是中等的题！！！明明是简单中的战斗简单啊。
除了该进制是加减而不是乘除之外，几乎没有任何难点。。。
map用于寻找，list用于循环。而list(dict.keys())是将所有key按定义顺序拿出来，并转换成list

'''

class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        map = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        for base in list(map.keys()):
            while num >= base:
                num = num - base
                result.append(map[base])
        return "".join(result)



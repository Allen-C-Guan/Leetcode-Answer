from typing import List
class Solution:
    def __init__(self):
        self.dic = {"2":["a","b","c"],
               "3":["d","e","f"],
               "4":["g","h","i"],
               "5":["j","k","l"],
               "6":["m","n","o"],
               "7":["p","q","r","s"],
               "8":["t","u","v"],
               "9":["w","x","y","z"]}
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not len(digits): return res
        self.helper(digits,"", res)
        return res

    def helper(self, digits: str, path: str, res: List[str]):
        if not len(digits):
            res.append(path)
            return
        for char in self.dic[digits[0]]:
            self.helper(digits[1:], path+char, res)



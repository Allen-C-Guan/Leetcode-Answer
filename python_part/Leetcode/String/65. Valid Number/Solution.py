class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        return self.isInt(s) or self.isFloatOrE(s)


    def isInt(self,s:str) -> bool: # int自带正负号功能
        try:
            int(s)
            return True
        except:
            return False
    def isFloatOrE(self,s:str) -> bool:  # float 自带e的功能！！wtf
        try:
            float(s)
            return True
        except:
            return False

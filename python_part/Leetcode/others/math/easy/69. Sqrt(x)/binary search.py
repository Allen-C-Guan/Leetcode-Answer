import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binary_search(1,x,x)

    def binary_search(self, lo, hi,key):

        if lo >= hi:
            if hi*hi > key:
                return hi-1
            else:
                return hi

        '''
        上面这个if else是解决该题的关键。
        '''

        mid = math.floor((lo + hi) / 2)
        res = mid * mid

        '''
        二分法最关键的地方就在于递归，而递归最关键的地方在于递归边界， 
        边界的+1 和 -1是为了保证递归一定会进入到递归出口，而不会出现无限递归的情况。
        '''
        if res == key:
            return mid
        elif res < key:
            return self.binary_search(mid+1,hi,key)
        else:
            return self.binary_search(lo,mid-1,key)






foo = Solution()
print(foo.mySqrt(2))
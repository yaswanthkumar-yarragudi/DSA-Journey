class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return x

        l = 1
        r = x
        ans  = 0
        
        while l<=r:
            m = (l+r)//2
            c = m*m
            if c==x:
                return m
            elif c<x:
                ans = m
                l = m+1 
            elif c>x:
                r = m-1
        return ans
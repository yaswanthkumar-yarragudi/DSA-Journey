class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x

        l = 0
        r = x-1
        ans =1

        while l<=r:
            m = (l+r)//2
            if m*m >x:
                r = m-1
            else:
                ans = m
                l = m+1
        return ans

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return n

        
        s = (n*(n+1))//2

        bs = 0

        for i in range(n,-1,-1):
            bs += i
            if bs == s:
                return i 
            s-=i



        return -1
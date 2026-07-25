class Solution:
    def maxProduct(self, n: int) -> int:
        a=[]
        while n>0:
            r = n%10
            n = n//10
            a.append(r)
        a.sort()
        return a[-1]*a[-2]
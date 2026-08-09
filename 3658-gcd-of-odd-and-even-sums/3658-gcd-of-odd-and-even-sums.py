class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n==1:
            return n

        a = n*(n+1)
        b = n**2


        while a>b:
            b,a=a,a%b
        return a

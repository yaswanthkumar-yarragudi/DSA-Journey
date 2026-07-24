class Solution:
    def mergeAlternately(self, s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        res = ''
        n = min(n1,n2)
        for i in range(n):
            res+=s1[i]+s2[i]

        if n1>n2:
            return res+s1[n:]
        else:
            return res+s2[n:]

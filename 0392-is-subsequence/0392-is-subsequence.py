class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s or s ==t:
            return True
        n1 = len(s)
        n2 = len(t)

        if n1>n2:
            return False
        
        p1 = 0 
        p2 = 0

        while p2<n2 and p1<n1:
            if s[p1] == t[p2]:
                p1+=1
                p2+=1
            else:
                p2+=1
                
        return p1 == n1 

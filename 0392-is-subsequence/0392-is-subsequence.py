class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if not t:
            return False

        def check (l,r,s,t):
            if l == len(s):
                return True
            if r == len(t):
                return False 
            if s[l] == t[r]:
                l+=1
            r+=1
            return check(l,r,s,t)

        return check(0,0,s,t)

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        if n != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        left = 0

        for i in range(n):
            if s[left] != t[left]:
                return False
            left+=1
        return True
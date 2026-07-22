class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)

        if n<=0:
            return True

        st = 0
        count = 0

        for i in t:
            if count<n and i == s[st]:
                st+=1
                count+=1
                if count == n:
                    return True

        return False


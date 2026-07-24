class Solution:
    def strStr(self, hay: str, needle: str) -> int:
        n = len(hay)
        m = len(needle)

        if n<m:
            return -1
        
        for i in range(n-m+1):
            if hay[i:i+m] == needle:
                return i
        return -1

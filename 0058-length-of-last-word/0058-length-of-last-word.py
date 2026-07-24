class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        length = 0

        for i in range(n-1,-1,-1):
            if  s[i] == ' ':
                return length
            length+=1
        return n
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ans = s.count('1')
        maxDelta = 0
        leftZeroes = 0
        i = 0
        while i < n:
            ones = 0
            rightZeroes = 0
            while  i < n and s[i] == '1':
                ones += 1
                i += 1
            while  i < n and s[i] == '0':
                rightZeroes += 1
                i += 1
            if leftZeroes and ones and rightZeroes:
                maxDelta  = max(leftZeroes + rightZeroes, maxDelta)
            leftZeroes = rightZeroes
        return ans + maxDelta
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        res = ''
        s.sort()

        first = s[0]
        last = s[-1]

        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return res
            res+=first[i]
        return res
        
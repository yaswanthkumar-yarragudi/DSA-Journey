class Solution:
    def reverseWords(self, s: str) -> str:
        if s == '':
            return ''
        res = ''
        s=s.split()
        for i in s :
            res=i+" "+res

        res = res.strip()
        return res

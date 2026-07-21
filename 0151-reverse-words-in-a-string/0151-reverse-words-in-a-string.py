class Solution:
    def reverseWords(self, s: str) -> str:
        if s == '':
            return ''
        a = s.split()
        a=a[::-1]
        return " ".join(a)

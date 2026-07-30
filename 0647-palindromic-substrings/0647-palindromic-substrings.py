class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        a=[]

        for i in range(n):
            word = ''
            for j in range(i,n):
                word = word+ s[j]

                if word ==word[::-1]:
                    a.append(word)
        return len(a)

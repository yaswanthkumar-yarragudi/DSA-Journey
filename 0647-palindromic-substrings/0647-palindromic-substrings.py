class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count =0

        for i in range(n):
            word = ''
            for j in range(i,n):
                word = word+ s[j]

                if word ==word[::-1]:
                    count+=1
        return count

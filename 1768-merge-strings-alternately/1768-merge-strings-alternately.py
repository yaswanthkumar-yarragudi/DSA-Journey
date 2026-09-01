class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n1= len(word1) 
        n2= len(word2) 

        if n1 == 0:
            return n2 
        elif n2 == 0:
            return n1

        i = 0
        ans = ''

        while i<n1 or i<n2:
            if i < n1:
                ans+=word1[i]
            if i < n2:
                ans+=word2[i]
            i+=1
            
        return ans
            
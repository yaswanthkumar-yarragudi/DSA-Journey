class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)

        r = min(l1,l2)
        new = ""

        for i in range(r):
            new += word1[i]
            new += word2[i]

        if len(word1) > len(word2):
            new+=word1[r:]
        else:
            new+=word2[r:]

        return new


        



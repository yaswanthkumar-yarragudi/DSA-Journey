class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False
        
        def check(word):

            d = {}

            for l in word:
                if l not in d:
                    d[l] = 1
                else:
                    d[l] += 1
            return d
    
        return sorted(list(check(word1).values())) == sorted(list(check(word2).values())) and sorted(list(check(word1).keys())) == sorted(list(check(word2).keys()))
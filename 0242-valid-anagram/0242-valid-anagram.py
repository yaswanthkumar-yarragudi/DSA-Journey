class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        if n != len(t):
            return False
        def check(word):
            freq = {}
            for l in word:
                if l in freq:
                    freq[l]+=1
                else:
                    freq[l] =1
            return freq
        s1 = check(s)
        t1 = check(t)
        return s1 == t1
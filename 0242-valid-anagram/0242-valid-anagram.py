class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        if n != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False

        return True
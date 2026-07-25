class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        n = len(a)
        res = ['a']*n

        for word in a:
            index = int(word[-1])-1
            res[index] = word[:-1]
        return " ".join(res)

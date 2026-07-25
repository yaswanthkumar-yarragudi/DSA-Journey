class Solution:
    def words(self,word):
        a = []
        n =len(word)

        for i in word:
            if i != '#':
                a.append(i)
            elif len(a)>0:
                a.pop()
                
        return "".join(a)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.words(s) == self.words(t)

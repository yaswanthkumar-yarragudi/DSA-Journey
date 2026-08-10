class Solution:
    def check(self, word, empty, l):
        n = len(word)
        if l == n :
            return empty
        empty = word[l] + empty
        l += 1
        return self.check(word,empty,l)        


    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        ans  = ''
        i = 0
        space = ' '
        for word in a:
            if i == len(a)-1:
                space = ''
            ans+=self.check(word,'',0)+space
            i+=1
        return ans
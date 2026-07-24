class Solution:
    def check(self,word):
        return word==word[::-1]
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return self.check(s[left:right]) or self.check(s[left+1:right+1])
        return True



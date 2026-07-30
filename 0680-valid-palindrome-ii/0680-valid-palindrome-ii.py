class Solution:

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                p1 = s[left:right]
                p2 = s[left+1:right+1]
                return p1 == p1[::-1] or p2 ==p2[::-1]
                
        return True



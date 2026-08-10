class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        def check(left,right):
            flag = False
            if left>right:
                return True
            if not s[left].isalnum():
                left+=1
                flag = True
            if not s[right].isalnum():
                right-=1
                flag = True
            if flag:
                return check(left,right)
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

            return check(left,right)

            
        return check(0,len(s)-1)
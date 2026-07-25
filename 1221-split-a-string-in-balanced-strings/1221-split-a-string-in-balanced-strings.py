class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=r=res=0

        for letter in s:
            if letter == 'R':
                r+=1
            if letter == 'L':
                l+=1
            if r == l:
                res+=1 
        return res
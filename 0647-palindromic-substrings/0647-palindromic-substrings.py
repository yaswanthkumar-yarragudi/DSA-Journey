class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count =0

        def check(left,  right):
            count = 0
            while left>=0 and right<n and s[left] == s[right]:
                count+=1
                left-=1
                right+=1
            return count
        
        for i in range(n):
            count+=check (i,i)
            count+=check(i,i+1)

        return count
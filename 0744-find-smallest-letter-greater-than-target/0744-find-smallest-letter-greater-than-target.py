class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)

        l = 0
        r = n-1
        ans = n

        while l<=r:
            m = (l+r)//2

            if letters[m] <= target:
                l = m+1
            elif letters[m] > target:
                ans = min(ans, m)
                r = m-1
            
        if ans == n:
            return letters[0]
        else:
            return letters[ans]

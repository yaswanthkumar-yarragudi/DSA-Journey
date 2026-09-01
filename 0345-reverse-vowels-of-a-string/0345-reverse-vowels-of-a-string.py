class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)

        vow = 'aeiouAEIOU'

        l = 0
        r = len(s)-1

        while l<r:
            if a[l] not in vow:
                l+=1
            if a[r] not in vow:
                r-=1
            if a[l] in vow and a[r] in vow:
                a[l],a[r] = a[r],a[l]
                l+=1
                r-=1
        return ''.join(a)    

            
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        a = []

        res = ""

        for i in s:
            if i in vowels:
                a.append(i)
        s=s[::-1]

        ind = 0
    
        for i in s:
            if i in vowels:
                res+=a[ind]
                ind+=1
            else:
                res+=i
        return res[::-1]


        
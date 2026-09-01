class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        a = s.split(" ")
        ans = ""
        print(a)
        for i in a:
            if i:
                ans = i+" "+ans
        return ans.strip()
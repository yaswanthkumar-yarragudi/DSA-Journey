class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        ans = ""
        print(a)
        for i in a:
            if i:
                ans = i+" "+ans
        return ans.strip()
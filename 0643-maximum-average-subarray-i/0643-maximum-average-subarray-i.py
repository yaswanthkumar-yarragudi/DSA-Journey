class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n =len(nums)
        cs =0

        for i in range(k):
            cs+=nums[i]

        ans =cs/k

        for i in range(k,n):
            cs = cs+nums[i]-nums[i-k]
            ans = max(ans,cs/k)
        return ans
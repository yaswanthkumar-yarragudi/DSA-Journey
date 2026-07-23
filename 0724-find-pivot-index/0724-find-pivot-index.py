class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ts = sum(nums)
        l = 0

        for i in range(n):
            r = ts - l - nums[i]
            if r == l:
                return i
            l+=nums[i]
        return -1
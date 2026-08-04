class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        h = max(nums)
        l = min(nums)
        l
        a = []
        res = []

        for i in range (l,h):
            if i not in nums:
                res.append(i)
        return res
                
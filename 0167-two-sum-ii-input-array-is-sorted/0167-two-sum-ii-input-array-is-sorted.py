class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            need = target - nums[i]
            if need in nums[i+1:]:
                return [i+1,nums[i+1:].index(need)+2+i]
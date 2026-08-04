class Solution:
    def canMakeArithmeticProgression(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()


        for i in range(n-2):
            if nums[i+1] -nums[i] == nums[i+2] - nums[i+1]:
                pass
            else:
                return False
        return True
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zp = 0
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[zp] = nums[zp],nums[i]
                zp+=1
                        
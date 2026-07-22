class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        st = 0

        for i in range(n):
            if nums[i]!=0:
                nums[st],nums[i] = nums[i],nums[st]
                st+=1
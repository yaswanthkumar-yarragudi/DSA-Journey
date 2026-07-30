class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 0
        n=len(nums)

        for i in range(n):
            if nums[i]!=0:
                nums[fast],nums[i]=nums[i],nums[fast]
                fast+=1
        return nums
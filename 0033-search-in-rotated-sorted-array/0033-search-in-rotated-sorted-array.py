class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        add =0
        flag = False
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                nums = nums[i:]+nums[:i]
                add = i
                break
        
        left = 0
        right = n-1

        while left<=right:
            mid = (left + right)//2

            if nums[mid] == target:
                return (mid+add)%n
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
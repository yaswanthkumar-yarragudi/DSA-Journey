class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(left,right):
            mid = (left+right)//2
            if left>right:
                return -1

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1

            return bs(left,right)
        return bs(0,len(nums)-1)

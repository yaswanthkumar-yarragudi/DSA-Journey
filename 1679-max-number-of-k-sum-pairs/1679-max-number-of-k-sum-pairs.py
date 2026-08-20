class Solution:
    def maxOperations(self, nums: List[int], tar: int) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        r = n-1
        count = 0

        while l<r:
            if nums[l] + nums[r] == tar:
                r-=1
                l+=1
                count +=1
            elif nums[l] +nums[r] > tar:
                r-=1
            else:
                l+=1
        return count
        
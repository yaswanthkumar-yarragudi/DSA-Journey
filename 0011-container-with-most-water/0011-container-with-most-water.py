class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        r = n-1
        water = 0
        max_water = 0 
        move = 1

        while l<r:
            p = min(nums[l],nums[r])
            water = p * (n-move)

            max_water =  max(max_water,water)

            if p == nums[l]:
                l+=1
            else:
                r-=1
            move+=1
        return max_water




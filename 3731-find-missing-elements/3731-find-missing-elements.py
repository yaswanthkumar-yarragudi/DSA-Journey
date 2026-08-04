class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)
        n = len(nums)
        nums.sort()
        i=low
        point = 0
        a = []
        
        while i<high:
            if i == nums[point]:
                i+=1
                point+=1
            else:
                a.append(i)
                i+=1
        return a
                
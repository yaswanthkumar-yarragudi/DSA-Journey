class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = list(set(nums))
 
        dup.sort()
        nums[:] = dup
        return len(set(dup))
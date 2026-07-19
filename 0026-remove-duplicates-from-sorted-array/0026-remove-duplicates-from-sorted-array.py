class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = sorted(list(set(nums)))
        nums[:] = dup
        return len(set(dup))
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dis1 = set(nums1)-set(nums2)
        dis2 = set(nums2)-set(nums1)
        return [list(dis1),list(dis2)]
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False
        
        a = float('inf')
        b = float('inf')

        for i in nums:
            if i <= a:
                a = i
            elif i <= b:
                b = i
            else:
                return True
                
        return False

        
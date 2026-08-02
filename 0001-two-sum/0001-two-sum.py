class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        n = len(nums)

        for i in range(n):
            need = target - nums[i]
            if need in freq:
                return [freq[need],i]
            freq[nums[i]] = i
            

                    
                

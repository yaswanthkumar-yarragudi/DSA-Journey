class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []

        for i in nums:
            need = target - i
            ind = (nums.index(i))

            if need in nums[ind+1:]:
                first = ind
                second = nums.index(need,ind+1)
                return [first,second]
        return []

                    
                

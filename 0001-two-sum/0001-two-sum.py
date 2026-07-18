class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []

        for i in nums:
            need = target - i
            ind = (nums.index(i))
            if need in nums[ind+1:]:
                first = nums.index(i)
                second = nums.index(need,ind+1)
                return [first,second]

                # if first != second:
                #     return [first,second]
                # try:
                #     first = nums.index(i)
                #     second = nums.index(need,first+1)            
                #     return [first,second]
                # except ValueError:
                #     pass
        return []

                    
                

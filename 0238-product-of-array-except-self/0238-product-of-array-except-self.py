class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_product = 1
        non_zero_product = 1
        ans = []

        if nums.count(0)>=2:
            return [0]*n
        
        for i in nums:
            zero_product*=i
            if i==0:
                continue    
            non_zero_product *= i

        for i in nums:
            if i==0:
                ans.append(non_zero_product)
            else:
                val = zero_product//i
                ans.append(val)


        return ans



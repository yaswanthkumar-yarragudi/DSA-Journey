class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        prod = 1
        zeros = nums.count(0)

        if 0 not in nums:
            for num in nums:
                prod*=num

            for num in nums:
                ans.append(prod//num)
            return ans
        else:
            if zeros >= 2:
                return [0]*n
            else:
                for num in nums:
                    if num != 0:
                        prod *=num
                for num in nums:
                    if num != 0:
                        ans.append(0)
                    else:
                        ans.append(prod)
                return ans


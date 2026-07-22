class Solution:
    def maxOperations(self, nums: List[int], tar: int) -> int:
        freq = {}
        count = 0
        
        for num in nums:
            need  = tar - num
            if need in freq and freq[need]>0:
                freq[need]-=1
                count+=1
            else:
                freq[num] = freq.get(num,0)+1
        return count


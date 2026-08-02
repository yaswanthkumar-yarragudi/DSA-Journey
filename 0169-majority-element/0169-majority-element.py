class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                freq[n]+=1


        return max(freq,key=freq.get) 


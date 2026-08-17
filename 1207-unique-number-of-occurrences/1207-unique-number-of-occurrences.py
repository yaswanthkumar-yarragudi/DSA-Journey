class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        di = {}
        n = len(nums)

        for i in range(n):
            if nums[i] not in di:
                di[nums[i]] = 1
            else:
                di[nums[i]] += 1
        print(list(di.values()),list(set(di.values())))
        return sorted(list(di.values()))==sorted(list(set(di.values())))
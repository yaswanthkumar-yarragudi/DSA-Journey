class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []

        n = len(candies)
        max_candies = max(candies)

        for i in range(n):
            if max_candies <= candies[i] + extraCandies:
                res.append(True)
            else:
                res.append(False)

        return res

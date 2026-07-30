class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        water = 0

        left = 0
        right = 0 
        maxL = []
        maxR = []

        for i in range(n):
            maxL.append(left)
            left = max(left,height[i])

        for i in range(n-1,-1,-1):
            maxR.append(right)
            right = max(right,height[i])
        maxR = maxR[::-1]

        for i in range(n):
            s = min(maxL[i],maxR[i])-height[i]
            if s>0:
                water+=s
        return water

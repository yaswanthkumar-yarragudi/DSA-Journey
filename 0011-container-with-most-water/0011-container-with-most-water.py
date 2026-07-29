class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        max_water = 0
        water = 0
        move =1

        low = 0 
        high = n-1

        while low<high:
            water = min(height[low],height[high])*(n-move)
            max_water = max(max_water,water)
            if height[low]<height[high]:
                low+=1
            else:
                high-=1
            move+=1
        return max_water

        
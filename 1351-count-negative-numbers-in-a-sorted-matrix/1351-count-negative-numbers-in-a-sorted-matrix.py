class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0

        for i in range(n):

            l = 0
            r = m-1
            
            while l<=r:
                mid = (l+r)//2
                if grid[i][mid]<0:
                    r = mid -1
                else:
                    l = mid+1
            count += m - l
        return count
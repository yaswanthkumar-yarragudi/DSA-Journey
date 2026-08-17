class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        ans = []

        for i in range(n):
            check = []
            for j in range(m):
                check.append(grid[j][i])
            ans.append(check)
        
        for li in grid:
            count += ans.count(li)

        return count


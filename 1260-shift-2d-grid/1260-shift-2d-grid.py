class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid)-1,len(grid[0])-1
        k%=((m+1)*(n+1))
        if k==0: return grid
        li=[]
        i,j,x,y,c=m,m,n,n,0
        while c!=k:
            li.append(grid[i][x])
            if x>=1: x-=1
            else:
                i-=1
                x=n
            c+=1
        while i!=0 or x!=-1:
            if x==-1:
                i-=1
                x=n
            if y==-1:
                j-=1
                y=n
            grid[j][y]=grid[i][x]
            x-=1
            y-=1
        i=0
        while k:
            if y==-1:
                j-=1
                y=n
            grid[j][y]=li[i]
            y-=1
            k-=1
            i+=1
        return grid
class Solution:
    def projectionArea(self, a: List[List[int]]) -> int:
        
        count=0
        n = len(a)
        

        for i in range(n):
            for j in range(n):
                if a[i][j]>0:
                    count+=1
                
            count+=max(a[i])    
    
        for j in range(n):
            mx  = 0 

            for i in range(n):
                mx = max(mx,a[i][j])
            count+=mx
        return count
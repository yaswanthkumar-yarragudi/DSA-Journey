class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo,hi = 1,num
        while lo <= hi:
            mid = (lo+hi)//2
            square = mid*mid
            if num == square:
                return True
            elif square >= num:
                hi = mid-1
            else :
                lo = mid+1
        return False


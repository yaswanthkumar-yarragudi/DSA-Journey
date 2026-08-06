class Solution:
    def smallestNumber(self, n: int, t: int) -> int:


        i = n

        while True:

            s =1
            temp =i
            while temp>0:
                r = temp%10
                s=s*r
                temp//=10

            if s%t ==0:
                return i
            i+=1
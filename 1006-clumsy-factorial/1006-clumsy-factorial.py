class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        op = 0

        for i in range(n - 1, 0, -1):

            if op == 0:          
                stack[-1] *= i

            elif op == 1:        
                stack[-1] = int(stack[-1] / i)

            elif op == 2:        
                stack.append(i)

            else:                
                stack.append(-i)

            op = (op + 1) % 4

        return sum(stack)
class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        for i in range(1, n + 1):
            if i * i == n:
                return True
            if i * i > n:
                break

        return False
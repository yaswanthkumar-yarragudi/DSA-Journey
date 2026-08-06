from collections import defaultdict
from math import gcd
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):

                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

       
                if dx == 0:
                    dy = 1

              
                elif dy == 0:
                    dx = 1

                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    if dx < 0:
                        dx *= -1
                        dy *= -1

                slopes[(dx, dy)] += 1

            curr = 1
            for cnt in slopes.values():
                curr = max(curr, cnt + 1)

            ans = max(ans, curr)

        return ans
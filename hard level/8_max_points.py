from typing import List


def get_kof(x1, y1, x2, y2):
    if x2 == x1:
        b = 0
        k = 1
        c = x2
    else:
        b = 1
        k = (y2 - y1) / (x2 - x1)
        c = y2 - k * x2
    return b, k, c


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        koefs = {}
        n = len(points)
        if n == 1:
            return 1
        max_ = 2
        for i in range(n - 1):
            x1, y1 = points[i]
            keys = set()
            for j in range(i + 1, n):
                x2, y2 = points[j]
                keys.add(get_kof(x1, y1, x2, y2))
            while keys:
                key = keys.pop()
                if key in koefs:
                    koefs[key] += 1
                    if max_ < koefs[key]:
                        max_ = koefs[key]
                else:
                    koefs[key] = 2

        return max_


a = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(Solution().maxPoints(a))
class Solution:
    def firstMissingPositive(self, x: List[int]) -> int:
        n = len(x)
        if n == 1:
            if x[0] == 1:
                return 2
            else:
                return 1
        i = 0
        while i < n:
            if x[i] >= 1 and x[i] <= n and x[i] != x[x[i] - 1]:
                x[x[i] - 1], x[i] = x[i], x[x[i] - 1]
                continue
            i += 1

        for i in range(n):
            if x[i] != i + 1:
                return i + 1
        return x[-1] + 1

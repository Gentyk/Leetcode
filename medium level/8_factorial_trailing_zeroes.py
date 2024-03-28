# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816/
# Вернуть количество нулей в n!
# надо посчитать количество 5к

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0

        count_5 = 0

        i = 5
        while i < n + 1:
            j = i
            while j % 5 == 0:
                count_5 += 1
                j = j // 5
            i += 5
        return count_5
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/

# необходимо хранить сет значений, потому что здля 2 зацикленность будет на 4ке

def get_new(t: int) -> int:
    new = (t % 10) ** 2
    b = t // 10
    while b:
        new += (b % 10) ** 2
        b = b // 10
    return new


class Solution:
    def isHappy(self, n: int) -> bool:
        keys = {n}  # it's important! we need to use set
        i = n
        while True:
            i = get_new(i)
            if i == 1:
                return True
            if i in keys:
                return False
            keys.add(i)

Solution().isHappy(2)
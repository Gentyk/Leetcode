# https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/813/

# прикол в том, чтобы менять элементы в массиве местами перед удалением и удалять последний

from random import randint


class RandomizedSet:

    def __init__(self):
        self.mass = []
        self.el_dict = dict()
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.el_dict:
            return False
        self.el_dict[val] = self.n
        self.mass.append(val)
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.el_dict:
            return False

        ind = self.el_dict[val]
        if ind != self.n - 1:
            self.mass[ind], self.mass[-1] = self.mass[-1], self.mass[ind]
            self.el_dict[self.mass[ind]] = ind
        del self.el_dict[val]
        del self.mass[-1]
        self.n -= 1
        return True

    def getRandom(self) -> int:
        ind = randint(0, self.n - 1)
        return self.mass[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
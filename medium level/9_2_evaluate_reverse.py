from typing import List


def do_it(a, b, action):
    if action == "+":
        return a + b
    if action == "-":
        return a - b
    if action == "*":
        return a * b
    return int(a / b)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        action = {'+', '-', '*', "/"}
        result = 0
        elems = []
        for i in tokens:
            if i in action:
                b = elems.pop()
                a = elems.pop()
                res = do_it(a, b, i)
                elems.append(res)
            else:
                elems.append(int(i))
        return elems[0]

print(Solution().evalRPN(["4","13","5","/","+"]))
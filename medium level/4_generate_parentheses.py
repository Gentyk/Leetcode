"""
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []

        def gen_(s, l, r):
            if l == 0 and r == 0:
                a.append(s)
            if l > 0:
                gen_(s + "(", l - 1, r)
            if l < r:
                gen_(s + ")", l, r - 1)

        gen_("", n, n)
        return a

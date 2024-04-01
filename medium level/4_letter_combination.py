class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        noks = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []

        for i in digits:
            sep = []
            if result == []:
                result = list(noks[i])
                continue
            for j in noks[i]:
                sep = sep + [r + j for r in result]
            result = sep

        return result
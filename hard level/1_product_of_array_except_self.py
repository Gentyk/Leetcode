class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for i in nums:
            if not a:
                a.append(i)
            else:
                a.append(a[-1] * i)
        for i in nums[::-1]:
            if not b:
                b.append(i)
            else:
                b.append(b[-1] * i)
        b.reverse()
        result = [b[1]]
        for i in range(1, len(nums) - 1):
            result.append(a[i - 1] * b[i + 1])
        result.append(a[-2])
        return result

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List


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

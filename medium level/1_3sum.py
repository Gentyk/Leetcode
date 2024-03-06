# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            c_s = -nums[i]
            s = set()
            for j in range(i + 1, n):
                required = c_s - nums[j]
                if required in s:
                    tt = (nums[i], required, nums[j])
                    if tt not in result:
                        result.add(tt)
                s.add(nums[j])

        return [list(i) for i in result]


# another solution, more long
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result = set()
#         n = len(nums)
#         for i in range(n-2):
#             j = i+1
#             k = n-1
#             while k>j:
#                 tt = (nums[i],nums[j],nums[k])
#                 if nums[i]+nums[j]+nums[k]==0 and tt not in result:
#                     result.add(tt)
#                     continue
#                 if -nums[i]<nums[j]+nums[k]:
#                     k-=1
#                     continue
#                 j+=1
#         return [list(i) for i in result]
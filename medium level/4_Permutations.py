# https://codersdaily.in/courses/leetcode/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) <= 1:
            return [nums]
        lst = []
        for i in range(len(nums)):

            key = nums[i]
            ost = nums[:i] + nums[i + 1:]

            for array in self.permute(ost):
                lst.append([key] + array)

        return lst

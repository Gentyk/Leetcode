from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_pos = 0
        for i in range(n - 1):
            if max_pos == i and nums[i] == 0:
                break
            if i + nums[i] > max_pos:
                max_pos = i + nums[i]
            if max_pos >= n - 1:
                break
        return max_pos >= n - 1


Solution().canJump([3,2,1,0,4])
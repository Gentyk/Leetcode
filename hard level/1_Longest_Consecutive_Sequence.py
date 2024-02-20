class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r = set(nums)
        max_ = 0
        for i in r:
            if i-1 in r:
                continue
            z = 1
            while i+z in r:
                z+=1
            max_ = max(z, max_)
        return max_
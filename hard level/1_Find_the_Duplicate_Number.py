class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]
        t = nums[0]
        h = nums[nums[0]]
        while t != h:
            t = nums[t]
            h = nums[nums[h]]

        t = 0
        while True:
            t = nums[t]
            h = nums[h]
            if t == h:
                return h
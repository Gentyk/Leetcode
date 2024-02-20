class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        c = {}
        n = len(nums1)
        for i in nums1:
            for j in nums2:
                r = i + j
                if r in c:
                    c[r] += 1
                else:
                    c[r] = 1
        sum_res = 0
        for i in nums3:
            for j in nums4:
                r = -1 * (i + j)
                if r in c:
                    sum_res += c[r]
        return sum_res

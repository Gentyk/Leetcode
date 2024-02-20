class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = (r-l)*min(height[r],height[l])
        while r>l+1:
            if height[r] > height[l]:
                l+=1
            else:
                r-=1
            res = max(res, (r-l)*min(height[r],height[l]))
        return res
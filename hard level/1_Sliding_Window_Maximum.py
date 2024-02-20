from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i - k + 1 > q[0]:
                q.popleft()
            if i >= k - 1:
                result.append(nums[q[0]])
        return result

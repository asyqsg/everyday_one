from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        size = len(nums)
        deq = deque()
        for i in range(k):
            if not deq:
                deq.append(nums[i])
            elif 

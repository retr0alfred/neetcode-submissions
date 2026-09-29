class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0
        curmax = totmax = float('-inf')
        while right < len(nums):
            curmax += nums[right]
            if nums[right] > curmax:
                left = right
                curmax = nums[right]
            totmax = max(curmax, totmax)
            right += 1
        return totmax
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        totmax = 0
        while left <= right:
            curmax = min(heights[left], heights[right]) * (right - left)
            totmax = max(totmax, curmax)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return totmax
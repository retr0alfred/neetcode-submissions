class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        totmax = float('-inf')
        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)
            totmax = max(volume, totmax)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return totmax
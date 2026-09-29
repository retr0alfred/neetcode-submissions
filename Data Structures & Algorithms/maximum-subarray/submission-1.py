class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0
        curmax = totmax = float('-inf')
        lst = []
        while right < len(nums):
            curmax += nums[right]
            lst.append(nums[right])
            if nums[right] > curmax:
                left = right
                curmax = nums[right]
                lst = []
            #curmax += nums[right]
            #lst.append(nums[right])
            totmax = max(curmax, totmax)
            right += 1
            #print(lst, curmax, totmax)
        return totmax
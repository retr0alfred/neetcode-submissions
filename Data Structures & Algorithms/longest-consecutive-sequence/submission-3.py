class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        totmax = 0

        for i in nums:
            if (i-1) not in checker:
                longest = 0
                while i+longest in checker:
                    longest += 1
                totmax = max(totmax, longest)
        return totmax
            
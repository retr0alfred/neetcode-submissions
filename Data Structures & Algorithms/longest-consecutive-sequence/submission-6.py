class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        longest = 0

        for i in nums:
            cur = 0
            if (i-1) not in checker:
                while i+cur in checker:
                    cur += 1
            longest = max(cur, longest)
        return longest
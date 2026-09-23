class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums):
            needed = target-value
            if needed in d:
                return [d[needed], index]
            d[value] = index
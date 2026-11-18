class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for cur, i in enumerate(nums):
            difference = target - i
            if difference in d1:
                return [d1[difference], cur]
            d1[i] = cur
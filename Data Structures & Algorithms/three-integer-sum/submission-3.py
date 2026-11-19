class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index, val in enumerate(nums):
            if index > 0 and nums[index - 1] == val:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                cal = val + nums[left] + nums[right]
                if cal > 0:
                    right -= 1
                elif cal < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
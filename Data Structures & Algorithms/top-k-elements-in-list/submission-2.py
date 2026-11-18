class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        res = []
        for i in nums:
            d1[i] = d1.get(i, 0) + 1
        reverse = sorted(d1.items(), key = lambda i:i[1], reverse = True)
        for i in range(k):
            res.append(reverse[i][0])
        return res
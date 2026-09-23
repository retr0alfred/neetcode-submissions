class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        totmax = 0
        while right <= len(prices) - 1:
            print(left, right)
            curmax = prices[right] - prices[left]
            totmax = max(totmax, curmax)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return totmax
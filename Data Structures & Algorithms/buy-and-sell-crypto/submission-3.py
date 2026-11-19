class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, profit = float('inf'), 0
        for i in prices:
            mini = min(i, mini)
            profit = max(profit, i - mini)
        return profit
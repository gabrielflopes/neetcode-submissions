class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        best = 0

        for price in prices[1:]:
            best = max(best, price - minBuy)
            minBuy = min(minBuy, price)

        return best
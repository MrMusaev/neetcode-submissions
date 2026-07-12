class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        lMinPrice = prices[0]
        for i in range(1, len(prices)):
            profits.append(prices[i] - lMinPrice)
            lMinPrice = min(lMinPrice, prices[i])

        return max(profits)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        n = len(prices)

        # Brute force solution
        for i in range(n):
            for j in range(i + 1, n):
                maxP = max(prices[j] - prices[i], maxP)

        return maxP
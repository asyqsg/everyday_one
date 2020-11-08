class Solution:
    def maxProfit(self, prices) -> int:
        size = len(prices)
        if size < 2: return 0
        dp = [-1 for i in range(size)]
        minprice = prices[0]
        max_get = 0
        for i in range(1,size):
            if prices[i] < minprice:
                minprice = prices[i]
                dp[i] = 0
            elif prices[i] >= minprice:
                dp[i] = prices[i] - minprice
            if dp[i] > max_get:
                max_get = dp[i]
        return max_get
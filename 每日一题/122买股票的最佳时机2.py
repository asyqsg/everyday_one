class Solution:
    def maxProfit(self, prices) -> int:
        size = len(prices)
        if size < 2: return 0
        dp = [0 for i in range(size)]

        for i in range(1,size):
            if prices[i] > prices[i-1]:
                if dp[i-1] >= 0:
                    dp[i] = dp[i-1]+prices[i]-prices[i-1]
                else:
                    dp[i] = prices[i] - prices[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]
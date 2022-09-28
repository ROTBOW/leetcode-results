class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
#         ans = 0
#         for idx in range(len(prices)):
#             for sell_day in range(idx+1, len(prices)):
#                 ans = max(ans, prices[sell_day]-prices[idx])
                
#         return ans
            
        left = 0 # Buy
        right = 1 # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] # our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
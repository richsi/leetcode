class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        buy = prices[0]

        for sell in prices[1:]:
            maxprofit = max(maxprofit, (sell-buy))

            if sell < buy:
                buy = sell
            
        return maxprofit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = float("-inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        total = 0
        for right, price in enumerate(prices):
            
            profit = prices[right] - prices[left]

            if profit > 0:
                total += profit
                left = right
            else:
                left = right

        return total
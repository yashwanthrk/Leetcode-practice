class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # buy = prices[0]
        # profit = 0

        # for i in range(1, len(prices)):
        #     buy = min(buy, prices[i])
        #     profit = max(prices[i] - buy, profit)

        # return profit


        # sliding window

        left = right = 0        
        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                print(prices[right], prices[left])
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            right += 1

        return max_profit

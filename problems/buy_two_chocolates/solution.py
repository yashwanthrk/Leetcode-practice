class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        # prices.sort()

        # initial_money = money
        # chocolates = 0
        # for price in prices:
            
        #     money = money - price
        #     chocolates += 1

        #     if chocolates == 2 and money >= 0:
        #         return money

        # return initial_money


        first_min = float("inf")
        second_min = float("inf")

        for price in prices:
            if first_min > price:
                second_min = first_min
                first_min = price
            elif second_min > price:
                second_min = price
        
        print(first_min, second_min)
        cost = money - (first_min + second_min) 
        return money if cost < 0 else cost
        
    
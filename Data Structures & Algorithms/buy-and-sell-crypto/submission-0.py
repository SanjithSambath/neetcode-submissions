class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        maximum_profit = 0
        lowest_number = prices[0]
        
        for price in prices: 

            if price < lowest_number:
                lowest_number = price
            
            if (price - lowest_number) > maximum_profit:
                maximum_profit = (price - lowest_number)
 
        return maximum_profit


        
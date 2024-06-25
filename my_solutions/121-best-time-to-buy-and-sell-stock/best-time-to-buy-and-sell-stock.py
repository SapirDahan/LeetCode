class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_Profit = 0
        minPrice = float('inf')

        for price in prices:
            # Update the minimum price so far
            if price < minPrice:
                minPrice = price
                
            # Calculate the potential profit and update maxProfit if it's higher
            elif price - minPrice > max_Profit:
                max_Profit = price - minPrice

        return max_Profit
        
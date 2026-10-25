class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit =0
        minPrice = prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            maxprofit = max(maxprofit,price-minPrice)
        return maxprofit
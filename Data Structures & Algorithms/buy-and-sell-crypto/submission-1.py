class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            maxProf = max(maxProf, price-minPrice)
        return maxProf
        
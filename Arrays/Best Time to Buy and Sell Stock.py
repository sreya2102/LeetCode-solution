class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        mi=prices[0]
        profit=0
        for i in prices:
            if i<mi:
                mi=i
            elif i-mi>profit:
                profit=i-mi
        return profit
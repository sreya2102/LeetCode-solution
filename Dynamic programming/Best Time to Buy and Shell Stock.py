class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        m=prices[0]
        p=0
        for i in prices:
            if i<m:
                m=i
            elif i-m>p:
                p=i-m
        return p

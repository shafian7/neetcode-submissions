class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mp = 0

        for i in range(len(prices) - 1):
            p = prices[i]
            ps = set(prices[i + 1:])
            mp = max(mp, max(ps) - p)

        
        return mp
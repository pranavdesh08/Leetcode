class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.profit = 0
        
        for buy in range(len(prices)-1):
        
            profit = max(prices[buy+1:]) - prices[buy]
                
            if self.profit < profit:
                self.profit = profit
                    
        return self.profit

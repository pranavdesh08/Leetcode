class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i=0
        buy=0
        sell=0
        profit=0
        
        while i < len(prices)-1:
            
            if prices[i] < prices[i+1]:
                buy = prices[i]
                
                for m in range(i+1,len(prices)):
                    if m == len(prices)-1:
                        sell = prices[m]
                        
                        i = m
                        break
                    elif prices[m] > prices[m+1]:
                        sell = prices[m]
                        
                        i = m + 1
                    
                        break
            else:
                i +=1
            profit += sell - buy
            sell=0
            buy=0
            
        return profit

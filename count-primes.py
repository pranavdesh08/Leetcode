class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n ==0 or n==1:
            return 0
        
        temp = [1]*n
        temp[0]=temp[1] = 0
        
        for i in range(2,n):
            
            if temp[i]==0:
                
                pass
            else:
                
                temp[i+i:n:i] = [0]*len(temp[i+i:n:i])
            
        return sum(temp)

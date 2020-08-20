class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <=1:
            return False
        
        tot=0
        for i in range(1,int(num**0.5)+1):
            
            if num % i==0:
                
                tot +=i
                if i*i !=num and i !=1:
                    
                    tot +=num/i
                    
                
        if tot == num:
            return True

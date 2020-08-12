class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for i in range(int(c**0.5)+1):
            
            b = c - i*i
            b = math.sqrt(b)
            if b == int(b):
                return True

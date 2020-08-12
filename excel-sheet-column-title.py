class Solution:
    def convertToTitle(self, n: int) -> str:
        
        alpha = string.ascii_uppercase
        cnt={}
        
        for i in range(len(alpha)):
            
            cnt[i] = alpha[i]
            
        if n <= 26:
            return cnt[n-1]
        else:
            
            title=''
            while n > 0:
                title += cnt[(n-1) % 26]
                n = (n-1) // 26
                
            return title[::-1]
                

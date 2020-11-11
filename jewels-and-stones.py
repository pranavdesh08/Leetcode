class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewel = list(J)
        cnt=0
        for i in S:
            
            if i in jewel:
                cnt +=1
                
        return cnt
                

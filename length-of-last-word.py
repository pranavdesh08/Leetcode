class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        tmp = s.split()
        
        n = len(tmp)-1
        
        if len(tmp) ==0:
            return 0
        
        return len(tmp[n])

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        x = min(strs,key=len)
        
        for ind,val in enumerate(x):
            
            for j in strs:
                if val != j[ind]:
                    return x[:ind]
        return x
               

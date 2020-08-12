class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        diff = ( (len(B)-1) // len(A) )+ 1
        print(diff)
        for i in range(2):
            print(A*(diff+i))
            if B in A*(diff+i) :
                return diff+i
            
        return -1

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        c=-1
        for i, j, k, l in itertools.permutations(A):
            
            hours = 10 * i + j
        
            minutes = 10 * k + l
            
            time = 60 * hours + minutes
            
            if 0 <= hours < 24 and 0 <= minutes < 60 and time> c:
                c = time
             
        return "{:02}:{:02}".format(*divmod(c,60)) if c>=0 else ""
            
                
            

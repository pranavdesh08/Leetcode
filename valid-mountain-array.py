class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        c_i=True
        i=0
        c_j=True
        j=len(A)-1
        
        if len(A) < 3:
            return False
        while c_i or c_j:
            
            if A[i] < A[i+1] and i < len(A)-2 and c_i:
                i+=1
            elif A[i] == A[i+1] and i < len(A)-2 and c_i:
                return False
            else:
                high1= A[i]
                ind_i = i
                c_i =False
                
            if A[j] < A[j-1] and i>0 and c_j:
                j -=1
            elif A[j] == A[j-1] and i>0 and c_j:
                return False
            else:
                high2= A[j]
                ind_j = j
                c_j =False
        if high1==high2 and ind_i == ind_j:
            return True

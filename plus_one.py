class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i=len(digits)-1
        
        while(i>-1):
            if digits[i]==9:
                digits[i]=0
                print(digits)
            else:
                digits[i]=digits[i]+ 1
                return(digits)
            i=i-1
        digits1=[1]
        digits1=digits1 + digits
        return(digits1)

class Solution:
    def reverse(self, x: int) -> int:
        
        rev=[]
        if x>(2**31)-1:
            return 0
        
        if x<-(2**31):
            return 0
        
        if x==0:
            return x
        
        if x<0:
            x=str(x)
            rev.append(x[0])
            x=int(x[1:])
            while x>0:
                rev.append(x%10)
                x=int(x/10)
            temp=int(''.join(map(str, rev)))
            
            if temp<-(2**31):
                return 0
            else:
                return temp
            
            
        else:
            while x>0:
                rev.append(str(x%10))
                x=int(x/10)
            temp=int(''.join(map(str,rev)))
            if temp>(2**31)-1:
                return 0
            else:
                return temp

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        self.array= None
        row = rowIndex
        
        
        if row < 5:
        #temp = 11**row
            self.array =[x for x in str(11**row)]
            return self.array
        
        temp =[int(x) for x in str(11**4)]
        
        if row >= 5:
            i = 5
            while i <= row:
                temp1=[1 for x in range(i+1) ]
                for k in range(1,i):
                    temp1[k] = temp[k] + temp[k-1]
                    
                temp = temp1
                i +=1    
            if i>row:
                return temp
                    

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        self.array = []
        row = numRows
        
        i = 1
        while i <= row:
            
            if i ==1:
                self.array.append([1])
                
            if i ==2:
                temp = [1,1]
                self.array.append(temp)
                
            if i > 2:
                
                temp1=[1 for index in range(i)]
                for k in range(1, i-1):
                    temp1[k] = temp[k-1] + temp[k]
                temp = temp1
                self.array.append(temp)
            i +=1
            
        return self.array

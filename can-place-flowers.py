class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            if flowerbed[0]==0 and n==1 or n ==0:
                return True
            elif flowerbed[0]==1 and n==0:
                return True
            else:
                return False
            
        if n == 0:
            return True
        
        valid = sum(flowerbed) + n
        if (-( len(flowerbed)// - 2)) >= valid:
            
            for index in range(len(flowerbed)):
                if flowerbed[index]==0:
                    if index == 0 and flowerbed[index + 1] == 0 :
                        flowerbed[index] = 1
                        n -= 1
                            
                    if index<len(flowerbed)-1 and index>0 and flowerbed[index + 1]== 0 and flowerbed[index - 1] == 0:
                        flowerbed[index] = 1
                        
                        n -=1
                        
                    if index == len(flowerbed) - 1 and flowerbed[index - 1] == 0 :
                        flowerbed[index] = 1
                        
                        n -= 1
        
                if n ==0:
                    break
                    
            if n !=0:
                return False
            else:
                return True
                 
        else:
            return False

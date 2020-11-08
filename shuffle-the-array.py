class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        if len(nums)==2:
            return nums
        arr=[]
        
        i=0
        j=0
        while i <len(nums):
            
            if i%2==0:
                arr.append(nums[j])
                j +=1
                
            else:
                arr.append(nums[n])
                n +=1
            
            i +=1
            
        return arr
                
        

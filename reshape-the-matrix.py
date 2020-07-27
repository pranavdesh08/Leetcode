class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        row = len(nums)
        no_ele = 0
        for i in range(row):
            
            no_ele += len(nums[i])
            
        if no_ele == r*c:
            
            m = []
            
            for j in range(row):
                
                m += nums[j]
            k=1
            reshape = []
            arr=[]
            for l in range(len(m)):
                
                arr.append(m.pop(0))
                if k ==c:
                    reshape.append(arr)
                    k =0
                    arr = []
                k +=1
            return reshape
        else:
            return nums
                
                
                

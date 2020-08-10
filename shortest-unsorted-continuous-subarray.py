class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        temp = sorted(nums)
        start = len(nums)
        end = 0 
        
        for i in range(len(nums)):
            
            if nums[i] != temp[i]:
                
                start = min(start,i)
                end = max(end,i)
                
        if end - start >= 0:
            
            return end - start +1
        else:
            return 0

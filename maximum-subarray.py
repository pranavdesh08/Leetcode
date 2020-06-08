class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sub_max=nums[0]
        current_int=0
        for i in nums:
            current_int=current_int + i
            if current_int>=sub_max:
                sub_max=current_int
            if current_int<0:
                current_int=0
        return sub_max
        
       

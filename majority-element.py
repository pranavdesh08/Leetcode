class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mid_value = len(nums)//2
        
        nums_set = set(nums)
        
        for i in nums_set:
        
            if nums.count(i)> mid_value:
                
                return i

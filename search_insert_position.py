class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        
        if target not in nums:
            if target>nums[len(nums)-1]:
                #nums.append(target)
                return len(nums)
            
            if target<nums[0]:
                return 0
        
            for i in range(len(nums)):
                if nums[i]>target:
                    return i

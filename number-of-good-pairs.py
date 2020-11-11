class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=0
        i=0
        while i<len(nums)-1:
            
            for j in range(i+1,len(nums)):
                
                if nums[i] == nums[j] and i < j:
                    cnt +=1
            i +=1
        return cnt

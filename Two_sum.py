class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}
        for index,ele in enumerate(nums):
            sub=target- ele
            
            if sub not in temp:
                temp[ele]=index
                
            else:
                return(temp[sub],index)

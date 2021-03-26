"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
 
Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        stay = 0
        print(nums)
        arr = []
        
        while stay < len(nums)-2:
            if nums[stay] > 0:
                break
                
            if stay != 0 and nums[stay] == nums[stay-1]:
                stay +=1
                continue
                
            start = stay + 1
            end = len(nums)-1
            
            while start < end:
                
                if nums[stay] + nums[start] + nums[end] == 0:
                    
                    tmp = [nums[stay] , nums[start] , nums[end]]
                    arr.append(tmp)
                    start +=1
                    end -=1
                    
                    while start < end and nums[start] == nums[start-1]:
                        start +=1
                    # while start < end and nums[end] == nums[end+1]:
                    #     end -=1
                   
                elif nums[stay] + nums[start] + nums[end] < 0:
                    start  += 1
                    
                else:
                    end -=1
            stay +=1
            
        return arr
                

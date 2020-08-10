class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            max(nums)
            
        arr = [float('-inf'),float('-inf'),float('-inf')]
        
        for i in nums:
            if i > arr[0]:
                arr[2]=arr[1]
                arr[1] = arr[0]
                arr[0] = i
            if i< arr[0] and i > arr[1]:
                arr[2] = arr[1]
                arr[1] = i
            
            if i < arr[0] and i < arr[1] and i > arr[2]:
                arr[2] = i
        print(arr)
        if arr[2] != float('-inf'):
            return arr[2]
        else:
            return max(arr)
        

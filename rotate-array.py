class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k <2:
            i = 0
            while i < k:
            
                temp = nums[len(nums)-1]
            
                for m in range(len(nums)-1,-1,-1):
                
                    nums[m] = nums[m-1]
                
                nums[0] = temp
            
                i +=1
                
        else:
            nums[:len(nums)] = nums[len(nums)-k:] + nums[:len(nums)-k]

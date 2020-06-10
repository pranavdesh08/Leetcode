class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        if n==0:
            return nums1
        
        if nums1[m-1] < nums2[0]:
            for i in nums2:
                nums1[m]= i
                m=m+1
            return nums1
        
        else:
            start=m
            for i in nums2:
                nums1[start]= i
                start=start+1
            
            
            
            for j in range(m+n):
                point=j
                
                k=j
                
                while k < (m+n) :
                    
                    if nums1[point]>= nums1[k]:
                        temp=nums1[k]
                        point=k
                    k=k+1
                nums1[point]=nums1[j]
                nums1[j]=temp

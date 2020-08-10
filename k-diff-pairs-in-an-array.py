class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt=0
        temp = {}
        for i in nums:
            temp[i] = temp.get(i,0)+1
            
        for i in temp:
            
            if k>0 and k + i in temp:
                cnt +=1
                
            elif k == 0 and temp[i]>1:
                cnt +=1
        return cnt

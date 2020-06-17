class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for index in range(len(numbers)-1):
            
            to_find = target - numbers[index]
            
            if to_find in numbers[index + 1:]:
                if to_find == numbers[index]:
                    
                    index2 = numbers[index+1:].index(to_find)
                    index2 = index + index2 + 1
                    return [index + 1,index2 + 1]
                    
                index2 = numbers.index(to_find)
                return [index + 1,index2 + 1]
        

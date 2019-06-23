class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = -99999999999
        max2 = -999999999999
        max_index = -1
        for index, number in enumerate(nums):
            if(number > max1):
                max1, max2 = number, max1
                max_index = index
            elif(number!= max1 and number > max2):
                max2 = number
                
        if(max1 >= 2*max2):
            return max_index
        return -1
        

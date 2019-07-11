#single pass hash-table with number as key and indexes as values.

from collections import defaultdict 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = defaultdict(lambda:[])
        
        for index, value in enumerate(nums):
            d[value].append(index)
            if(2*value == target):
                if(len(d[target - value]) > 1):
                    return [d[target - value][0],index]
            elif(len(d[target - value]) >= 1):
                return [d[target - value][0],index]
        
        

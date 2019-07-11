from collections import defaultdict

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = defaultdict(lambda:0)
        
        for number in nums:
            if(d[number] == 1):
                return True
            d[number] += 1
            
        return False

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        value = 1
        
        while(value < n):
            value *= 2
        
        if(value == n):
            return True
        
        return False

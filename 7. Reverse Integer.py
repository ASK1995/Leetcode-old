class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        
        if(x < 0):
            x = -x
            neg = True
            
        x = str(x)
        x = x[::-1]
        x = int(x)
        
        if(x < -2**31 or x > 2**31 - 1):
            return 0
        
        if(neg):
            return -x
        return x
        

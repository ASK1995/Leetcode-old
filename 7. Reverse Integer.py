class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        
        if(x < 0):
            neg = True
            x = -x
            
        reversed_int = 0
        
        while(x != 0):
            reversed_int = reversed_int*10 + x%10
            x = x//10
            
        if(neg):
            reversed_int *= -1
        if(reversed_int < (-2)**31 or reversed_int > (2**31) - 1):
            return 0
        return reversed_int

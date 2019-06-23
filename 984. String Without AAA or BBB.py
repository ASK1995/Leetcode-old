class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if(A == 0):
            return "b" * B
        elif(B == 0):
            return "a" * A
        elif(A == B):
            return "ab" + self.strWithout3a3b(A-1, B-1)
        elif(A > B):
            return "aab" + self.strWithout3a3b(A-2, B-1)
        elif(A < B):
            return "bba" + self.strWithout3a3b(A-1, B-2)
        
        

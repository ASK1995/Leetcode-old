class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        neg_index = -1
        for index, value in enumerate(A):
            A[index] = value*value
            if(value < 0):
                neg_index = index
        if(neg_index == -1):
            return A
        
        p1 = neg_index
        p2 = neg_index+1
        res = []
        while(p1 >= 0 and p2 < len(A)):
            if(A[p1] <= A[p2]):
                res.append(A[p1])
                p1 -= 1
            else:
                res.append(A[p2])
                p2 += 1
        while(p1 >= 0):
            res.append(A[p1])
            p1 -= 1
        while(p2 < len(A)):
            res.append(A[p2])
            p2 += 1
        
        return res

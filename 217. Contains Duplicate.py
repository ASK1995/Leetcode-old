from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(lambda:0)
        for i in nums:
            if(d[i] > 0):
                return True
            d[i] += 1
        return False

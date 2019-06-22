#single pass hash-table with number as key and indexes as values.

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(lambda:[])
        res = []
        for index,num in enumerate(nums):
            d[num].append(index)
            if(target == 2*num):
                if(len(d[num])>= 2):
                    for i in d[num]:
                        res.append(i)
                    return res
            elif(target != num*2 and len(d[target - num]) >= 1):
                res.append(d[target-num][0])
                res.append(index)
                return res

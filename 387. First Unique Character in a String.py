from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(lambda : 0)
        for i in s:
            d[i] += 1
        for index, value in enumerate(s):
            if(d[value] == 1):
                return index
        return -1

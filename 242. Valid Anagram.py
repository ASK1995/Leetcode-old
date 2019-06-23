from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(lambda:0)
        for i in s:
            d[i] += 1
        for i in t:
            if(d[i] > 0):
                d[i] -= 1
            else:
                return False
        return (all(values == 0 for values in d.values()) )

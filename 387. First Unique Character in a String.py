from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(lambda:0)
        
        for letter in s:
            d[letter] += 1
        
        for index,value in enumerate(s):
            if(d[value] == 1):
                return index
        
        return -1

from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = defaultdict(lambda:0)
        
        for letter in s:
            d[letter] += 1
        
        for letter in t:
            if(d[letter] == 0):
                return False
            d[letter] -= 1
        
        for key, value in d.items():
            if(value > 0):
                return False
            
        return (all(values == 0 for values in d.values()) )

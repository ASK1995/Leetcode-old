from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ""):
            return 0    
        
        if(len(s) == len(set(s))):
            return len(s)
        
        index0 = 0
        d = defaultdict (lambda : 0)
        count = 0
        max_count = 0
        
        for index,value in enumerate(s):
            if(d[value] == 1):
                if(count > max_count):
                    max_count = count
                count = 0
                
                while(d[value] == 1):
                    d[s[index0]] -= 1
                    index0 += 1
                    
            d[value] += 1
            count = index - index0 + 1 
            
        return max(count, max_count)
            

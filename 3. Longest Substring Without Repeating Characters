from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ""):
            return 0    
        i0 = 0
        res = 1
        current_string = ""
        for index, letter in enumerate(s):
            current_string += letter
            if(len(current_string) == len(set(current_string))):
                res = max(res, index - i0 + 1)
            else:
                while(len(current_string) != (len(set(current_string)))):
                    i0 += 1
                    current_string = current_string[1:]
        res = max(res, len(s) - i0)
        return res  
		
    def lengthOfLongestSubstring2(self, s: str) -> int:
        d = defaultdict(lambda:0)
        j = 0
        count = max_count = 0
        for index,value in enumerate(s):
            if(d[value] == 1):
                if(count > max_count):
                    max_count = count
                count = 0
                while(d[value] == 1):
                    d[s[j]] -= 1
                    j += 1
            d[value] += 1
            count = index - j + 1 
            
        if(count > max_count):
            return count
        return max_count
            

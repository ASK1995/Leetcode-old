class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        current = []
        openers = set(['(', '[', '{'])
        closers = set([')', ']', '}'])
        
        for bracket in s:
            if(bracket in openers):
                current.append(bracket)
            else:
                if(len(current) == 0):
                    return False
                elif(bracket == "}" and current[-1] == "{"):
                    current.pop()
                elif(bracket == "]" and current[-1] == "["):
                    current.pop()
                elif(bracket == ")" and current[-1] == "("):
                    current.pop()
                else:
                    return False
                
        if(len(current) == 0):
            return True
        return False
            

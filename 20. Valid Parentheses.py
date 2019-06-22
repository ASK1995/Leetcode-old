class Solution:
    def isValid(self, s: str) -> bool:
        starters = set(["(", "[", "{"])
        enders = set([")", "}", "]"])
        stack_s = []
        for i in s:
            if(i in starters):
                stack_s.append(i)
            elif(i in enders and len(stack_s) != 0):
                if(stack_s[-1] == "(" and i == ')' ):
                    stack_s.pop()
                elif(stack_s[-1] == "[" and i == ']' ):
                    stack_s.pop()
                elif(stack_s[-1] == "{" and i == '}' ):
                    stack_s.pop()
                else:
                    return False
            else:
                return False
        if(len(stack_s) == 0):
            return True
        return False

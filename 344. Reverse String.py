class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for index in range(len(s)//2):
            s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]
        

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for letter in str:
            if(letter >= 'A' and letter <= 'Z'):
                res.append(chr(ord(letter) + 32))
            else:
                res.append(letter)
        return "".join(res)

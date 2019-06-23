from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = set(["!", "?", ".", ";", ",", "'"])
        for i in s:
            while(i in paragraph):
                paragraph = paragraph.replace(i, " ")
        
        ban_set = set(banned)
        d = defaultdict(lambda:0)
        paragraph = paragraph.lower()
        paragraph = paragraph.split(" ")
        
        for word in paragraph:
            if(word not in ban_set and word != ""):
                d[word] += 1
        
        max_word_count = max(d.values())
        
        l = []
        
        for key,value in d.items():
            if(value == max_word_count):
                l.append(key)
        return l[0]
    

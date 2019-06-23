from collections import defaultdict

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = defaultdict(lambda:0)
        for email in emails:
            local, domain = email.split("@")
            while("." in local):
                local = local.replace(".","")
            for index in range(len(local)):
                if(local[index] == "+"):
                    local = local[:index]
                    break
            d[local + "@" + domain] += 1
        return len(d)
                
            

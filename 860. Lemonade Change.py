class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twentys = 0
        
        for bill in bills:
            if(bill == 5):
                fives += 1
            elif(bill == 10):
                if(fives >= 1):
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                if(fives >= 1 and tens >= 1):
                    fives -=1
                    tens -=1 
                    twentys +=1 
                elif(fives >= 3):
                    fives -= 3
                    twentys += 1
                else:
                    return False
        return True

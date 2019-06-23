class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for number in range(left, right+1):
            flag = True
            check_number = number
            while(number != 0):
                digit = number%10
                number //= 10
                if(digit != 0 and check_number%digit == 0):
                    continue
                else:
                    flag = False
            if(flag):
                res.append(check_number)
        return res

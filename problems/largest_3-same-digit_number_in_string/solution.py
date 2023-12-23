class Solution:
    def largestGoodInteger(self, num: str) -> str:


        for digit in "9876543210":
            if digit not in num:
                continue
            

            index = num.find(f'{digit}{digit}{digit}')
            if index != -1:
                if num.count(digit) >= 3:
                    return f'{digit}{digit}{digit}'
        

        return ""


        
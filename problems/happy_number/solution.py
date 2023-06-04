class Solution:
    
    def isHappy(self, n: int) -> bool:
        
        def check_happy_number(n):
            print(n)
            if n > 1 and n < 7 or n in [8, 9]:
                return False

            if n == 1 or n == 7:
                return True

            # n = str(n)
            # sum = 0
            # for x in n:
            #     sum += (int(x) ** 2)
            n = str(n)
            sum_val = sum(int(x) ** 2 for x in n)
           
            return check_happy_number(sum_val)

        return check_happy_number(n)

        # def recursive_call(n, loop_dict):
            
        #     n = str(n)
            
        #     if n in loop_dict:
        #         return False
        #     else:
        #         loop_dict[n] = True

        #     sum = 0
        #     for num in (n):
        #         num = int(num)
        #         sum += (num * num)
    
    
    
        #     if sum == 1:
        #         return True
        #     else:
        #         # reapeat the recursion
        #         # check if its the infinite loop
        #         return recursive_call(sum, loop_dict)
        # return recursive_call(n, {})

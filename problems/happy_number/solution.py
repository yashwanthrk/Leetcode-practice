class Solution:
    
    def isHappy(self, n: int) -> bool:
        
        def recursive_call(n, loop_dict):
            
            n = str(n)
            
            if n in loop_dict:
                return False
            else:
                loop_dict[n] = True

            sum = 0
            for num in (n):
                num = int(num)
                sum += (num * num)
    
    
    
            if sum == 1:
                return True
            else:
                # reapeat the recursion
                # check if its the infinite loop
                return recursive_call(sum, loop_dict)
        return recursive_call(n, {})


        
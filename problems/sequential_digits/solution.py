class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def generateSequential(start, num):
            
            if num > high:
                return
            
            if low <= num <= high:
                sequence_list.append(num)
            
            if start < 9: 
                
                #  important
                num =  num * 10 + start + 1
                generateSequential(start + 1, num)

        sequence_list = []
        for i in range(1, 10):
            generateSequential(i, i)
       
        sequence_list.sort()
        
        return sequence_list

       
        
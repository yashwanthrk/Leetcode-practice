class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []  

        for i, temp in enumerate(temperatures):
            
            # Pop indices from the stack while the current temperature is higher than the temperatures at those indices
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                # calculate the number of days
                result[prev_index] = i - prev_index  
            stack.append(i)  

        return result
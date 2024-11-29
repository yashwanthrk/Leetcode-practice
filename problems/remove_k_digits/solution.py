class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Remove digits from the stack while k > 0 and stack top is greater than the current digit
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            # Push the current digit onto the stack
            stack.append(digit)
        
        # Remove remaining digits if k > 0
        while k > 0:
            stack.pop()
            k -= 1
        
        # Build the result string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # If result is empty, return "0"
        return result if result else "0"
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:

            if char != ']':
                stack.append(char)

            else:
                
                substr = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                
                # Remove the '[' character
                stack.pop()
                
                # Build the repeat count
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                # Repeat the substring k times and push back to the stack
                stack.append(int(k) * substr)
        
        return "".join(stack)

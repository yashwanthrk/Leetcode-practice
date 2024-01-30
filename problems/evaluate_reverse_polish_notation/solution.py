class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            
            if token in ['+', '-', '*', '/']:
                
                second_token = stack.pop()
                first_token = stack.pop()

                if token == '+':
                    stack.append(first_token + second_token)
                elif token == '-':
                    stack.append(first_token - second_token)
                elif token == '*':
                    stack.append(first_token * second_token)
                elif token == '/':
                    # For division, convert to int for floor division in Python
                    stack.append(int(first_token / second_token)) 
            else:
                stack.append(int(token))

        return stack[-1]
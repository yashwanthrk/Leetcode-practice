class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    #     dummy_stack = []
    #     for token in tokens:
    #         try:
    #             token = int(token)
    #             dummy_stack.append(int(token))
    #         except:
    #             num2 = dummy_stack.pop()
    #             num1 = dummy_stack.pop()
    #             if token == "+":
    #                 result = self.rpn_add(num1, num2)
    #             elif token == "-":
    #                 result = self.rpn_sub(num1, num2)
    #             elif token == "*":
    #                 result = self.rpn_multiply(num1, num2)
    #             else:
    #                 result = int(self.rpn_divide(num1, num2))
                
    #             dummy_stack.append(result)

    #     return dummy_stack[0]
                


    # def rpn_add(self, num1, num2):
    #     return num1 + num2
    
    # def rpn_sub(self, num1, num2):
    #     return num1 - num2
        
    # def rpn_multiply(self, num1, num2):
    #     return num1 * num2
    
    # def rpn_divide(self, num1, num2):
    #     return int(float(num1) / (num2))




        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        
        return stack[-1]


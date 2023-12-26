class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """


        stack = []

        operators = ["+", "-", "*", "/"]

        for token in tokens:
            
            if token in operators and len(stack) > 1:
                
                second_num = stack.pop()
                first_num = stack.pop()

                result = 0
                
                if token == "+":
                    result = first_num + second_num
                elif token == '-':
                    result = first_num - second_num
                elif token == "*":
                    result = first_num * second_num
                else:
                    result = int(float(first_num) / second_num)
                
                stack.append(result)

            else:
                stack.append(int(token))
        

        return stack.pop()
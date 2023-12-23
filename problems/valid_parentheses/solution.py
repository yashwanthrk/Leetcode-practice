class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        parenthesis_dict = { ')' : '(' ,  "}" :  "{" ,    "]" : "[" }

        for ch in s:
            if ch not in parenthesis_dict:
                stack.append(ch)
                
            elif stack and stack[-1] == parenthesis_dict[ch]:
                stack.pop()
            
            else:
                stack.append(ch)

            

        return len(stack) == 0



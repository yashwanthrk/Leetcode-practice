class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parentheses_dict = { "}" : "{", ")" : "(", "]" : "["}

        for c in s:
            if c not in parentheses_dict:
                stack.append(c)
            else:
                if stack and stack[-1] == parentheses_dict[c]:
                    stack.pop()
                else:
                    return False
                

        return len(stack) == 0



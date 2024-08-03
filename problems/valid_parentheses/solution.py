class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False

        parentheses_dict = {
            '}': '{',
            ']' : '[',
            ')' : '('
        }

        stack = []

        for ch in s:
            if ch in parentheses_dict:
                if stack and stack[-1] == parentheses_dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return not stack
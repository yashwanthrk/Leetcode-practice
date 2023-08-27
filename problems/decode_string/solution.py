class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ""
                while stack[-1] != '[':
                    # only alphabets are concatenated now
                    # order of concatenation is important
                    substr = stack.pop() + substr
                # pop last element which is '['
                stack.pop()

                k = ""
                # pop digits which is 0 - 9
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)


        return "".join(stack)

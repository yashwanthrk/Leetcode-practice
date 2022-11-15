class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        dict_parentheses = {'}':'{', ')':'(', ']':'['}        
        for bracket in s:
            if bracket in dict_parentheses.values():
                l.append(bracket)
            else:
                if len(l) > 0 and l[-1] == dict_parentheses[bracket]:
                        l.pop()
                else:
                    return False

        return len(l) == 0

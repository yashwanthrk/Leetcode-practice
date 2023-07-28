class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        prev_num = float('-inf')
        
        for word in words:
            if word.isdigit():
                if int(word) <= prev_num:
                    return False
                prev_num = int(word)
                
        return True

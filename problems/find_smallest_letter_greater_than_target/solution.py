class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        target_val = ord(target)

        for i in range(1, 26):
            if chr(target_val + i) in letters:
                return chr(target_val + i)
        
        return letters[0]
        
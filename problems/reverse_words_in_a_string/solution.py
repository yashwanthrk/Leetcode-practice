class Solution:
    def reverseWords(self, s: str) -> str:

        # words = s.strip().split() 
        # return ' '.join(reversed(words))

        # Note - just reverse the order of words, not characters

        s = s.split()  # This will automatically handle extra spaces
        result = ""
        for i in range(len(s) - 1, -1, -1):
            if i != 0:
                result = result + s[i] + " "
            else:
                result = result + s[i]   
        return result
class Solution:
    def reverseWords(self, s: str) -> str:
       
     # reverse the word, not the character    

       # string to array
       # trims whitesapces also  
        s = s.split()

        new_s = ""
        for index in range(len(s) - 1, -1, -1):
            print(s[index])
            if index != 0:
                new_s += s[index] + " "
            else:
                new_s += s[index]

        return new_s
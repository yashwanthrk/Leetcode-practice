class Solution:
    def reverseVowels(self, s: str) -> str:
        

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        new_str = list(s)

        while i < j:
            if new_str[i] in vowels and new_str[j] in vowels:
                new_str[i], new_str[j] = new_str[j], new_str[i]
                i += 1
                j -= 1
            elif new_str[i] not in vowels:
                i += 1
            elif new_str[j] not in vowels:
                j -= 1

        return ''.join(new_str)



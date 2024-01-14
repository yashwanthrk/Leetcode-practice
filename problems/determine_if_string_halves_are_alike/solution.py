class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        # a = s[:len(s) // 2]
        # b = s[len(s) // 2:]

        # a_vowel_count = 0
        # b_vowel_count = 0


        # for ch1, ch2 in zip(a, b):
        #     if ch1 in vowels:
        #         a_vowel_count += 1
        #     if ch2 in vowels:
        #         b_vowel_count += 1

        # return a_vowel_count == b_vowel_count


        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        half_length = len(s) // 2

        a_vowel_count = sum(1 for ch in s[:half_length] if ch in vowels)
        b_vowel_count = sum(1 for ch in s[half_length:] if ch in vowels)

        return a_vowel_count == b_vowel_count
            


                
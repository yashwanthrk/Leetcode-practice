class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def calculate_character_frequencies(word):
            # Initialize an array to store the frequencies of characters
            frequencies = [0] * 26
            unique_characters = set()
            
            for char in word:
                char_index = ord(char) - ord('a')
                unique_characters.add(char)
                frequencies[char_index] += 1
            return unique_characters, frequencies

        
        unique_chars1, freq1 = calculate_character_frequencies(word1)
        unique_chars2, freq2 = calculate_character_frequencies(word2)

        # Check if the sets of unique characters are the same
        if unique_chars1 != unique_chars2:
            return False
        
        # Check if the sorted frequency arrays are the same
        return sorted(freq1) == sorted(freq2)


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        if not words:
            return []

        prev_word_sorted = ''.join(sorted(words[0]))
        anagram_list = [words[0]]

        for word in words[1:]:
            sorted_word = ''.join(sorted(word))
            if sorted_word != prev_word_sorted:
                anagram_list.append(word)
                prev_word_sorted = sorted_word

        return anagram_list
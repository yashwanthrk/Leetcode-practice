from collections import Counter, defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        total_count = 0
        char_dict = Counter(chars)

        for word in words:
            count = 0
            cur_ch = defaultdict(int)

            good_word = True
            for ch in word:
                cur_ch[ch] += 1
                if ch not in char_dict or cur_ch[ch] > char_dict[ch]:
                    good_word = False
                    break
            
            if good_word:
                total_count += len(word)
            


        return total_count
                                    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:


        hash_map = {}

        for ch in ransomNote:
            if ch in hash_map:
                hash_map[ch] += 1 
            else:
                hash_map[ch] = 1
        
        for ch in magazine:
            if ch in hash_map and hash_map[ch] != 0:
                hash_map[ch] -= 1
        print(hash_map)
        return sum(hash_map.values()) == 0
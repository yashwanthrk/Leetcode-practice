class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = {}
        
        for ch in ransomNote:
            ransomNoteDict[ch] = ransomNoteDict.get(ch, 0) + 1

        for ch in magazine:
            if ch in ransomNoteDict and ransomNoteDict[ch] > 0:
                ransomNoteDict[ch] -= 1

        if sum(ransomNoteDict.values()) <= 0:
                return True

        return False
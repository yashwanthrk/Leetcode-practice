class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groups = defaultdict(list)
    
        for string_str in strs:
            sorted_string = ''.join(sorted(string_str))
            
            anagram_groups[sorted_string].append(string_str)

      
        return list(anagram_groups.values())
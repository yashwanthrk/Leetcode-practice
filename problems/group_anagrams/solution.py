class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                # ord(char): This part of the expression converts a character (e.g., 'a', 'b', etc.) into its corresponding ASCII value. 
                # For instance, the ASCII value of 'a' is 97.
# ord('a'): This is a constant value, 97, which is the ASCII value of the letter 'a'.
                count[ord(char) - ord('a')] += 1
            
            # Convert the count list to a tuple to use as a dictionary key
            key = tuple(count)

            
            if key not in result:
                result[key] = []

            result[key].append(s)
        
        return list(result.values())

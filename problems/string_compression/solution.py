class Solution:
    def compress(self, chars: List[str]) -> int:
        
        result = []

        i = 0

        while i < len(chars):
            char = chars[i]
            count = 1
            
            # Count the number of consecutive characters
            while i + 1 < len(chars) and chars[i + 1] == char:
                count += 1
                i += 1
            
            result.append(char)
            
            if count > 1:
                result.extend(list(str(count)))
            
            i += 1

        for j in range(len(result)):
            chars[j] = result[j]
        
        return len(result)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:


        if len(s) < 10:
            return []


        
        seen, result = set() , set()


        for i in range(len(s) - 9):
            new_s = s[i:i+10]

            if new_s in seen:
                result.add(new_s)
            
            else:
                seen.add(new_s)


        return list(result)

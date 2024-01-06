class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""
        
        for index in range(len(strs[0])):
            for word in strs:
                if index == len(word) or strs[0][index] != word[index]:
                    return result

            result += strs[0][index]


        return result 
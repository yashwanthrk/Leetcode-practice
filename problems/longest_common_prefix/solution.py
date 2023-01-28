class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for ch_tuple in zip(*strs):
            if len(set(ch_tuple)) == 1: 
                output += ch_tuple[0]
            else:
                return output
        return output
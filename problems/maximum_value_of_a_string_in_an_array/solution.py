class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        def extract_string(ele):
            if ele.isdigit():
                return int(ele)

            return len(ele)
        count = 0        
        for ele in strs:
            curr_count = extract_string(ele)
            if count < curr_count:
                count = curr_count
        return count



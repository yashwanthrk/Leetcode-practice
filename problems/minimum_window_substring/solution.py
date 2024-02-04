class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        window_counts = {}


        required = len(dict_t)
        formed = 0

        
        l, r = 0, 0
        
        # result tuple of the form (window length, left, right)
        result = float("inf"), None, None

        while r < len(s):

            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]
                
                # Save the smallest window until now.
                if r - l + 1 < result[0]:
                    result = (r - l + 1, l, r)

                # The character at the position pointed by the `Left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1    

            r += 1    
            
        return "" if result[0] == float("inf") else s[result[1]:result[2] + 1]
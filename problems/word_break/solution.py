class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
                
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented

        # loop till n + 1, as i exclusive during substring
        for i in range(1, n + 1):
            for j in range(i):
                # s[j:i] , j inclusive and i is exclusive
                if dp[j] and s[j:i] in wordDict:
                    print(j, i, s[j:i])
                    dp[i] = True
                    break   # No need to check further for this i

        return dp[n]



        # refer again
        
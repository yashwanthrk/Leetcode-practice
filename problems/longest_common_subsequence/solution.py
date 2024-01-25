class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        N = len(text1)
        M = len(text2)

        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

        output = 0
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


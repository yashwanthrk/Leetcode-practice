class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        row_len = len(text1)
        col_len = len(text2)

        dp = [[0] * (col_len + 1) for _ in range(row_len +1)]
        

        for row in range(1, row_len + 1):
            for col in range(1, col_len + 1):
                if (text1[row - 1] == text2[col - 1]):
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return dp[-1][-1]

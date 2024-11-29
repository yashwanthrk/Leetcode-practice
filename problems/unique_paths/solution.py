class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # queue = deque([(0, 0)])  # Start from the top-left corner
        # count = 0  # To count unique paths

        # # Perform BFS
        # while queue:
        #     x, y = queue.popleft()
            
        #     # If we reach the bottom-right corner, increment the count
        #     if x == m - 1 and y == n - 1:
        #         count += 1
        #         continue

        #     # Move down
        #     if x + 1 < m:
        #         queue.append((x + 1, y))

        #     # Move right
        #     if y + 1 < n:
        #         queue.append((x, y + 1))

        # return count


        # # # Memoization dictionary
        # # memo = {}

        # # def dfs(i, j):
        # #     # Base cases
        # #     if i == 0 or j == 0:
        # #         return 1  # Only one path along the edges
            
        # #     # If already computed, return the cached value
        # #     if (i, j) in memo:
        # #         return memo[(i, j)]
            
        # #     # Recursive computation
        # #     memo[(i, j)] = dfs(i - 1, j) + dfs(i, j - 1)
        # #     return memo[(i, j)]

        # # # Start from bottom-right corner
        # # return dfs(m - 1, n - 1)


        dp = [[0] * n for _ in range(m)]  # Initialize a 2D array with zeros

        # Step 2: Initialize the first row and first column
        for i in range(m):
            dp[i][0] = 1  # Only one way to move vertically
        for j in range(n):
            dp[0][j] = 1  # Only one way to move horizontally

        # Step 3: Fill the DP table using the recurrence relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Step 4: Return the result from the bottom-right corner
        return dp[m-1][n-1]
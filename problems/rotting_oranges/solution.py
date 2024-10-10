class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        from collections import deque
        
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        EMPTY, FRESH, ROTTEN = 0, 1, 2
        fresh_oranges = 0

        # Step 1: Count fresh oranges and enqueue all rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh_oranges += 1

        # Edge case: If there are no fresh oranges, return 0 (no time required)
        if fresh_oranges == 0:
            return 0

        # Step 2: Initialize BFS variables
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0

        # Step 3: Perform BFS to rot adjacent fresh oranges
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # If the adjacent cell is a fresh orange, rot it and enqueue it
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == FRESH:
                        grid[new_row][new_col] = ROTTEN
                        fresh_oranges -= 1
                        queue.append((new_row, new_col))

            # Only increment minutes if there are still oranges to process
            if queue:
                minutes += 1

        # Step 4: If there are still fresh oranges left, return -1
        return minutes if fresh_oranges == 0 else -1
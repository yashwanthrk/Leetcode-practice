class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j)) 
                elif grid[i][j] == 1:
                    fresh_oranges += 1  

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2  
                        fresh_oranges -= 1  
                         # Add newly rotten orange to the queue
                        queue.append((new_row, new_col))
            
            if queue:
                minutes += 1

        return minutes if fresh_oranges == 0 else -1
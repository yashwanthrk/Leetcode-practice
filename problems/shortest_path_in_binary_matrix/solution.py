class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1

        if grid[0][0] == 1:
            return -1

        from collections import deque
        
        rows, cols = len(grid), len(grid[0])



        def bfs(grid, start):

          # Start is a tuple (x, y)   
            queue = deque([start]) 
            visited = set()
            visited.add(start)
            
            # Define directions: (row_change, col_change)
            directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Top-left diagonal
        (-1, 1),  # Top-right diagonal
        (1, -1),  # Bottom-left diagonal
        (1, 1)    # Bottom-right diagonal
    ]

            while queue:
                x, y, dist = queue.popleft()

                if x == rows - 1 and y == cols - 1:
                    return dist



                # Process the current cell
                print(f"Visiting: {x}, {y}")

                for dr, dc in directions:
                    nx, ny = x + dr, y + dc  # Compute neighbor's coordinates

                    # Check if neighbor is within bounds and not visited
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0:
                        queue.append((nx, ny, dist + 1))
                        visited.add((nx, ny))

            return -1

        return bfs(grid, (0, 0, 1))


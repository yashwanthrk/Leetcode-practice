class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        

        from collections import deque

        m, n = len(grid), len(grid[0])


        # (x, y, steps, obstacles_removed)
        queue = deque([(0, 0, 0, 0)])  
        
        visited = set((0, 0, 0))

        while queue:
            
            x, y, steps, obstacles_removed = queue.popleft()
            
            # If target is reached
            if x == m - 1 and y == n - 1:
                return steps
            
            #  The problem specifies that you can remove at most  k obstacles. If new_obstacles > k, then the current path is invalid because you’ve exceeded the allowed number of obstacle removals.

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:  
#                     If you ignore new_obstacles <= k, the algorithm might return a path where more than  k obstacles are removed, which is not allowed by the problem.

                    new_obstacles = obstacles_removed + grid[nx][ny]
                    
                    if new_obstacles <= k and (nx, ny, new_obstacles) not in visited:
                        visited.add((nx, ny, new_obstacles))
                        queue.append((nx, ny, steps + 1, new_obstacles))
        
        return -1  

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        from collections import deque

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1


        directions = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])

        while queue:

            x, y, path_len = queue.popleft()

            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return path_len

            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if  0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if (new_x, new_y) not in visited and grid[new_x][new_y] != 1:
                        queue.append((new_x, new_y, path_len + 1))
                        visited.add((new_x, new_y))

        
        return -1


#         Time Complexity: O(n²) (where n is the grid dimension), as each cell is visited at most once.
# Space Complexity: O(n²) for the queue and visited set




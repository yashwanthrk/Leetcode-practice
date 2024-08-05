class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()

        islands = 0    
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # Check bounds and if the cell is water or visited
            if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == '0' or
            (r, c) in visited):
                return

            # Mark the cell as visited
            visited.add((r, c))
            # Visit all adjacent cells (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands
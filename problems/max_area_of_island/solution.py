class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
         
        # visited_island = set()
        # max_area = 0

        # def check_for_neighbouring_lands(x, y):

        #     # will see if the lands we are checking comes under the boundary / grid
        #     if x < 0 or x >= m or y < 0 or y >= n:
        #         return 0

        #     if (x, y) in visited_island:
        #         return 0

        #     if grid[x][y] == 0:
        #         return 0

        #     visited_island.add((x, y))
            
        #     area = 1

        #     area += check_for_neighbouring_lands(x + 1, y)
        #     area += check_for_neighbouring_lands(x - 1, y)
        #     area += check_for_neighbouring_lands(x, y + 1)
        #     area += check_for_neighbouring_lands(x, y - 1)

        #     # print(area, x, y)

        #     return area
        

        # m = len(grid)
        # n = len(grid[0])
        
        # for x in range(m):
        #     for y in range(n):
        #         if grid[x][y] == 1 and (x, y) not in visited_island:
        #             area = check_for_neighbouring_lands(x, y)
        #             max_area = max(max_area, area)


        # return max_area


        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r, c + 1) + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # maxArea = max(maxArea, bfs(r, c))
                    maxArea = max(maxArea, dfs(r, c))


        return maxArea



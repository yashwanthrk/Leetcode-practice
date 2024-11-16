class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited_island = set()

        def check_for_neighbouring_lands(x, y):

            # will see if the lands we are checking comes under the boundary / grid
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0

            if (x, y) in visited_island:
                return 0

            if grid[x][y] == "0":
                return 0

            visited_island.add((x, y))

            # When you recurse into the neighboring cells, you do the same thing for each new land cell. You never reset area back to 1 because in the current scope of each recursive call, you're always adding the value returned by each subsequent recursive call.
            area = 1

            area += check_for_neighbouring_lands(x + 1, y)
            area += check_for_neighbouring_lands(x - 1, y)
            area += check_for_neighbouring_lands(x, y + 1)
            area += check_for_neighbouring_lands(x, y - 1)

            return area

        
        num_of_islands = 0

        m = len(grid)
        n = len(grid[0])
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and (x, y) not in visited_island:
                    num_of_islands += 1
                    check_for_neighbouring_lands(x, y)

        return num_of_islands


        # Time
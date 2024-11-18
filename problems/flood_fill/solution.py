class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:  # No need to process if color is already set
            return image

        ROW, COL = len(image), len(image[0])  # Dimensions of the grid
        old_color = image[sr][sc]  # Color to be replaced

        def fill_color(x, y):
            # Check bounds and if the cell matches the old color
            if x < 0 or x >= ROW or y < 0 or y >= COL or image[x][y] != old_color:
                return

            # Update the cell's color
            image[x][y] = color

            # Recursively call fill_color for adjacent cells
            fill_color(x - 1, y)
            fill_color(x + 1, y)
            fill_color(x, y - 1)
            fill_color(x, y + 1)

        fill_color(sr, sc)  # Start the flood fill from the starting cell
        return image

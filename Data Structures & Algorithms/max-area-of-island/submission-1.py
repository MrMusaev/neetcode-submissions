class Solution:
    def withinBoundary(self, grid, row_i, col_i) -> bool:
        return 0 <= row_i < len(grid) and 0 <= col_i < len(grid[row_i])
    
    # Calculate an area of an island using DFS
    def calculateAreaDfs(self, grid: List[List[int]], row_i: int, col_i: int) -> int:
        # 5. Mark the land as visited and current area as one
        grid[row_i][col_i] = -1
        area = 1

        # 6. Define directions to check next
        # right, bottom, left, top
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # 7. Try every direction from the current land to find more islands
        for direction in directions:
            # 8. Calculate the cordinations of new point
            new_row_i, new_col_i = row_i + direction[0], col_i + direction[1]

            # 9. Check if they are within grid boundaries
            if not self.withinBoundary(grid, new_row_i, new_col_i):
                continue

            # 10. Continue DFS if new land found, increasing the area            
            if grid[new_row_i][new_col_i] == 1:
                area += self.calculateAreaDfs(grid, new_row_i, new_col_i)
        
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1. Set up
        max_area = 0

        # 2. Iterate through the grid until a land is found
        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                if grid[row_i][col_i] == 0:
                    continue
                
                # 3. When a land is found calculate its area using DFS
                found_area = self.calculateAreaDfs(grid, row_i, col_i)
                
                # 4. Update max area 
                max_area = max(max_area, found_area)
        
        return max_area
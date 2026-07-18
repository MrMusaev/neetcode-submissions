class Solution:
    def withinBoundary(self, grid, row_i, col_i):
        return 0 <= row_i < len(grid) and 0 <= col_i < len(grid[row_i])

    def updateDistancesDFS(self, grid, row_i, col_i, cur_distance):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for direction in directions:
            new_row_i, new_col_i = row_i + direction[0], col_i + direction[1]

            if not self.withinBoundary(grid, new_row_i, new_col_i):
                continue
            
            if grid[new_row_i][new_col_i] <= 0:
                continue
            
            if cur_distance + 1 < grid[new_row_i][new_col_i]:
                grid[new_row_i][new_col_i] = cur_distance + 1
                self.updateDistancesDFS(grid, new_row_i, new_col_i, cur_distance + 1)
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                if grid[row_i][col_i] == 0:
                    self.updateDistancesDFS(grid, row_i, col_i, 0)
class Solution:
    def withinBoundary(self, grid: List[List[str]], row_i, col_i) -> bool:
        return 0 <= row_i < len(grid) and 0 <= col_i < len(grid[row_i])

    def dfs(self, grid: List[List[str]], row_i: int, col_i: int) -> None:
        # change current island to -1 to mark it as visited 
        grid[row_i][col_i] = '-1'

        # we need to check 4 directions to find more islands
        # we go right, bottom, left, top
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for direction in directions:
            new_row_i = row_i + direction[0]
            new_col_i = col_i + direction[1]

            # check if indexes are within the grid boundaries
            if not self.withinBoundary(grid, new_row_i, new_col_i):
                continue
            
            # perform dfs on the new found land
            if grid[new_row_i][new_col_i] == '1':
                self.dfs(grid, new_row_i, new_col_i)
        

    def numIslands(self, grid: List[List[str]]) -> int:        
        # set up 
        n_islands = 0

        # iterate through the grid and find any land
        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                # when we find a land we perform dfs and change its values to '-1's
                # then increase number of islands
                if grid[row_i][col_i] == '1':
                    self.dfs(grid, row_i, col_i)
                    n_islands += 1
        
        return n_islands
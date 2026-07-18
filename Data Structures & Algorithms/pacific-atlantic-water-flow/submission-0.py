class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def withinBoundary(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        
        def dfs(r, c, visited, previous):
            if (r, c) in visited or not withinBoundary(r, c) or heights[r][c] < previous:
                return
            
            visited.add((r, c))
            
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in directions:
                new_r, new_c = r + d[0], c + d[1]
                dfs(new_r, new_c, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        result = pacific.intersection(atlantic)

        return [[r, c] for r, c in result]
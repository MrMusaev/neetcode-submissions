class Solution:
    def withinBoundaries(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[r]) 

    def orangesRotting(self, grid: List[List[int]]) -> int:
        cur_minutes, fresh_fruits = 0, 0
        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruits += 1
        
        while queue and fresh_fruits > 0:
            cur_minutes += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for d in directions:
                    next_r, next_c = r + d[0], c + d[1]

                    if not self.withinBoundaries(grid, next_r, next_c) or grid[next_r][next_c] == 0:
                        continue
                    
                    if grid[next_r][next_c] == 1:
                        # mark fruit as rotten
                        grid[next_r][next_c] = 2
                        fresh_fruits -= 1
                        queue.append((next_r, next_c))

        return cur_minutes if fresh_fruits == 0 else -1
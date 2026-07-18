class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        cur_distance = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # 1. Find all treasure points and add them into the queue 
        for r_i in range(len(grid)):
            for c_i in range(len(grid[r_i])):
                if grid[r_i][c_i] == 0:
                    queue.append((r_i, c_i))
        
        # 2. Use level-order BFS to determine the distance from each treasure 
        # to neighbour lands
        while queue:
            # 3. Update distance in each step
            cur_distance += 1

            # 4. Try different directions for each treasure
            for _ in range(len(queue)):
                r_i, c_i = queue.popleft()

                for d in directions:
                    next_r, next_c = r_i + d[0], c_i + d[1]
                    
                    if not self.withinBoundaries(grid, next_r, next_c) or grid[next_r][next_c] == -1:
                        continue
                    
                    if cur_distance < grid[next_r][next_c]:
                        grid[next_r][next_c] = cur_distance
                        queue.append((next_r, next_c))
    
    def withinBoundaries(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[r])





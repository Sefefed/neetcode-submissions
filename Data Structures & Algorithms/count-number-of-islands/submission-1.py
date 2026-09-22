from collections import deque
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        cntIslnds = 0 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        def bfs(r, c):
            queue.append((r, c))
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = '0'

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cntIslnds += 1
                    grid[i][j] = '0'
                    bfs(i, j)
        return cntIslnds            



                  
       




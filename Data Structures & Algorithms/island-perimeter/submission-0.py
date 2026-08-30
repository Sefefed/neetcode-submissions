class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        perimeter = 0
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r, c):
            nonlocal perimeter
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                for x, y in dir:
                    nr, nc = row + x, col + y
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) in visited:
                        continue 
                    elif 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                    else:
                        perimeter += 1      
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 1:
                    visited.add((i, j))
                    bfs(i, j)
        return perimeter            

        
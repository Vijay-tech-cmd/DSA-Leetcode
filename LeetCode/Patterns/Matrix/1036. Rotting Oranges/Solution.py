class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        visit = [[0] * m for _ in range(n)]
        count_fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    visit[i][j] = 2
                    queue.append((i, j, 0))
                else:
                    visit[i][j] = 0
                if grid[i][j] == 1:
                    count_fresh += 1
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        tm = 0
        count = 0
        while queue:
            row, col, t = queue.popleft()
            tm = max(tm, t)
            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visit[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                     queue.append((nrow, ncol, t+1))
                     visit[nrow][ncol] = 2
                     count += 1
        if count_fresh != count:
            return -1
        return tm
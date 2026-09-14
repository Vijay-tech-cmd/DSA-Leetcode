class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        iniColor = image[sr][sc]
        ans = image
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        if iniColor == color:
            return image
        def dfs(row, col):
            ans[row][col] = color
            n = len(image)
            m = len(image[0])
            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]
                if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and image[nrow][ncol] == iniColor and ans[nrow][ncol] != color):
                    dfs(nrow, ncol)
        dfs(sr, sc)
        return ans
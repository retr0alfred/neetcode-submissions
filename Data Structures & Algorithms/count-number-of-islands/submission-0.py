class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= column or grid[i][j] == '0':
                return False
            else:
                grid[i][j] = '0'
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        for i in grid:
            print(*i)
        return count
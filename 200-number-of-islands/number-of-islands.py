class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == '0':
                return

            seen.add((row, col))
            for r, c in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(row + r, col + c)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    res += 1
                    dfs(row, col)

        return res
        

class neighborSum:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.positions = {grid[i][j]: (i, j) for i in range(self.n) for j in range(self.n)}

    def adjacentSum(self, value):
        if value not in self.positions:
            return 0
        i, j = self.positions[value]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_sum = 0

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total_sum += self.grid[ni][nj]

        return total_sum

    def diagonalSum(self, value):
        if value not in self.positions:
            return 0
        i, j = self.positions[value]
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        total_sum = 0

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total_sum += self.grid[ni][nj]

        return total_sum


# Example
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = neighborSum(grid)
print(obj.adjacentSum(2))
print(obj.diagonalSum(2))

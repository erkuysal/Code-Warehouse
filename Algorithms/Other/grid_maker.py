class CoordinatePlane:
    def __init__(self, n):
        self.n = n
        self.plane = [[0 for _ in range(n)] for _ in range(n)]

    def set_value(self, x, y, value):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.plane[x][y] = value
        else:
            raise IndexError("Coordinates are out of bounds")

    def get_value(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            return self.plane[x][y]
        else:
            raise IndexError("Coordinates are out of bounds")

    def print_plane(self):
        for row in self.plane:
            print(' '.join(map(str, row)))


# Example usage
n = 5
plane = CoordinatePlane(n)
# plane.set_value(2, 2, 1)
# plane.set_value(0, 0, 5)
# plane.set_value(4, 4, 9)

print("Coordinate Plane:")
plane.print_plane()
from dataclasses import dataclass
from typing import Generic, TypeVar, Sequence

T = TypeVar("T")


@dataclass
class Point(Generic[T]):
    x: int
    y: int
    val: T

    def coords(self):
        return (self.y, self.x)

    def __str__(self):
        return self.val


class Grid():
    def __init__(self, lines: list[str]):
        self.points = [[Point(x, y, int(val) if val.isdigit() else val) for x, val in enumerate(line)]
                       for y, line in enumerate(lines)]
        self.height = len(lines)
        self.width = len(lines[0])
        print(self.points)

    def draw(self):
        for row in self.points:
            for col in row:
                print(col, end="")
            print()

    def get_point(self, x: int, y: int):
        return self.points[y][x]

    def get_left(self, x: int, y: int):
        if x == 0:
            return None
        return self.get_point(x - 1, y)

    def get_right(self, x: int, y: int):
        if x == self.width - 1:
            return None
        return self.get_point(x + 1, y)

    def get_above(self, x: int, y: int):
        if y == 0:
            return None
        return self.get_point(x, y - 1)

    def get_below(self, x: int, y: int):
        if y == self.height - 1:
            return None
        return self.get_point(x, y + 1)

    def get_top_left(self, x: int, y: int):
        above = self.get_above(x, y)
        left = self.get_left(x, y)
        if not above or not left:
            return None
        return self.get_point(left.x, above.y)

    def get_top_right(self, x: int, y: int):
        above = self.get_above(x, y)
        right = self.get_right(x, y)
        if not above or not right:
            return None
        return self.get_point(right.x, above.y)

    def get_bottom_left(self, x: int, y: int):
        below = self.get_below(x, y)
        left = self.get_left(x, y)
        if not below or not left:
            return None
        return self.get_point(left.x, below.y)

    def get_bottom_right(self, x: int, y: int):
        below = self.get_below(x, y)
        right = self.get_right(x, y)
        if not below or not right:
            return None
        return self.get_point(right.x, below.y)

    def __str__(self):
        for row in self.points:
            for col in row:
                print(col, end="")
            print()


if __name__ == '__main__':
    grid = Grid(["OXX", "XOX", "XXX"])
    grid.draw()

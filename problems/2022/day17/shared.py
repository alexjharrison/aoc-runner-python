import pathlib
from os import getenv


class Grid:
    def __init__(self):
        self.occupied: set[tuple[int, int]] = set([(x, 0) for x in range(0)])
        self.y_max = 0

    def touchdown(self, tetro_pts: set[tuple[int, int]]):
        self.y_max = max(self.y_max, *[y for x, y in tetro_pts])
        self.occupied |= tetro_pts


class Tetronimono:
    def __init__(self, ant: int, grid: Grid):
        self.points: set[tuple[int, int]] = set()
        self.has_stopped = False
        self.grid = grid
        self.offset_top = 0

        start_x = 2
        start_y = grid.y_max + 4
        if ant % 5 == 0:
            for x in range(start_x, start_x + 4):
                self.points.add((x, start_y))
        elif ant % 5 == 1:
            for y in range(start_y, start_y + 3):
                self.points.add((start_x + 1, y))
            for x in range(2, 5):
                self.points.add((x, start_y + 1))
        elif ant % 5 == 2:
            for x in range(start_x, start_x + 3):
                self.points.add((x, start_y))
            for y in range(start_y + 1, start_y + 3):
                self.points.add((start_x + 2, y))
        elif ant % 5 == 3:
            for y in range(start_y, start_y + 4):
                self.points.add((start_x, y))
        elif ant % 5 == 4:
            for x in range(start_x, start_x + 2):
                for y in range(start_y, start_y + 2):
                    self.points.add((x, y))

    def go_left(self):
        for x, y in self.points:
            if (x - 1, y) in self.grid.occupied or x == 0:
                return
        self.points = set([(x - 1, y) for x, y in self.points])

    def go_right(self):
        for x, y in self.points:
            if (x + 1, y) in self.grid.occupied or x == 6:
                return
        self.points = set([(x + 1, y) for x, y in self.points])

    def go_down(self):
        for x, y in self.points:
            if (x, y - 1) in self.grid.occupied or y == 1:
                self.has_stopped = True
                self.grid.touchdown(self.points)
                return
        self.points = set([(x, y - 1) for x, y in self.points])

    def print(self):
        max_y = max([y for x, y in self.points])
        for row in range(max_y, 0, -1):
            print("|", end="")
            for col in range(7):
                char = "."
                if (col, row) in self.points:
                    char = "@"
                elif (col, row) in self.grid.occupied:
                    char = "#"
                print(char, end="")
            print("|")
        print("+-------+\n")


def _format_dataset(dataset: "list[str]"):
    return dataset[0]


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

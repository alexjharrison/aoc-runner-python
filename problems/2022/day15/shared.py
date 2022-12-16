import pathlib
from os import getenv
from re import findall
from dataclasses import dataclass

# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


@dataclass
class Point:
    x: int
    y: int
    b: tuple[int, int]
    dist: int

    def range_at_line(self, row: int) -> set[tuple[int, int]]:
        dy = abs(row - self.y)
        dx = abs(self.dist - dy)
        return set([(x, row) for x in range(self.x - dx, self.x + dx + 1) if dy <= self.dist])

    def range_limits_at_line(self, row: int) -> tuple[int, int]:
        dy = abs(row - self.y)
        dx = abs(self.dist - dy)
        return (self.x - dx, self.x + dx + 1)


def _format_dataset(dataset: "list[str]"):
    pts: list[Point] = []
    for line in dataset:
        s_x, s_y, b_x, b_y = [int(n)
                              for n in findall(r'-?\d+\.?\d*', line)]
        dist = abs(b_x - s_x) + abs(b_y - s_y)
        pts.append(Point(s_x, s_y, (b_x, b_y), dist))
    return pts


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"
# file = "/dataset.txt" if getenv("USE_FULL") else "/dataset.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

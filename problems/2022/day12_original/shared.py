import pathlib
from os import getenv, system
from string import ascii_lowercase
from time import sleep

width = 0
height = 0


class Node:
    def __init__(self, value: int, x: int, y: int, is_target: bool):
        self.value = value
        self.coords = (x, y)
        self.neighbors: list[Node] = []
        self.is_target = is_target
        self.steps_to_here = width * height

    def __str__(self):
        return str(self.coords) + ' ' + str(len(self.neighbors))


def shortest_path_distance(
    parent_node: Node,
    current_path: set[tuple[int, int]] = set()
) -> int | None:
    system("clear")
    debug_grid = [list("." * width) for _ in range(height)]
    for x, y in current_path:
        debug_grid[y][x] = "#"
    for row in debug_grid:
        for char in row:
            print(char, end="")
        print()
    # sleep(.05)

    if parent_node.is_target:
        return len(current_path)

    if parent_node.coords in current_path:
        return None

    if parent_node.steps_to_here < len(current_path):
        return None
    parent_node.steps_to_here = len(current_path)

    current_path.add(parent_node.coords)

    shortest_distance = width * height
    for neighbor in parent_node.neighbors:
        neighbor_shortest_distance = shortest_path_distance(
            neighbor, current_path)
        if neighbor_shortest_distance is not None:
            # if neighbor.coords in current_path:
            # print(neighbor_shortest_distance, neighbor.coords)
            current_path.discard(neighbor.coords)

        shortest_distance = min(
            shortest_distance, neighbor_shortest_distance) if neighbor_shortest_distance is not None else shortest_distance

    return shortest_distance


def _format_dataset(dataset: "list[str]"):
    grid: dict[tuple[int, int], Node] = {}
    S, E = (0, 0), (0, 0)
    for row_idx, row in enumerate(dataset):
        for col_idx, letter in enumerate(row):
            global width, height
            width = len(dataset[0])
            height = len(dataset)
            value = 0
            if letter in ascii_lowercase:
                value = ascii_lowercase.index(letter)
            elif letter == 'E':
                value = 25
                E = (col_idx, row_idx)
            else:
                S = (col_idx, row_idx)
            grid[(col_idx, row_idx)] = Node(
                value, col_idx, row_idx, letter == "E")

    return grid, S, E, len(dataset), len(dataset[0])


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset.txt"
# file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset(reverse=True):
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

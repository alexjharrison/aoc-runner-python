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
        self.visited = False

    def __str__(self):
        return str(self.coords) + ' ' + str(len(self.neighbors))


def shortest_path_distance(
    start_node: Node,
    end_node: Node,
) -> int:
    queue: list[tuple[Node, int]] = [(start_node, 0)]
    levels: list[int] = []
    visit_order: list[tuple[int, int]] = []
    while len(queue) > 0:
        target_node, level = queue.pop(0)
        visit_order.append(target_node.coords)
        levels.append(level)
        if not target_node.visited:
            target_node.visited = True

            if target_node.coords == end_node.coords:
                return level
            for neighbor in target_node.neighbors:
                if not neighbor.visited:
                    queue.append((neighbor, level + 1))
    return width * height


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
# file = "/dataset.txt" if getenv("USE_FULL") else "/dataset.txt"
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset(reverse=True):
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

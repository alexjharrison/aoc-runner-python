import pathlib
from os import getenv
from itertools import cycle


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    obstacles: set[tuple[int, int]] = set()
    for line in dataset:
        coord_pairs = line.split(' -> ')
        prev = (int(coord_pairs[0].split(',')[0]),
                int(coord_pairs[0].split(',')[1]))
        for coord_pair in coord_pairs:
            x, y = [int(pt) for pt in coord_pair.split(',')]
            x1, x2 = sorted([x, prev[0]])
            y1, y2 = sorted([y, prev[1]])
            if x1 == x2:
                obstacles |= set(zip(cycle([x1]), range(y1, y2 + 1)))
            else:
                obstacles |= set(zip(range(x1, x2 + 1), cycle([y1])))
            prev = (x, y)
    return obstacles


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

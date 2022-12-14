import pathlib
from os import getenv
from json import loads


def compare_pairs(first, second) -> int:
    match first, second:
        case int(), int():
            return second - first
        case list(), int():
            return compare_pairs(first, [second])
        case int(), list():
            return compare_pairs([first], second)
        case list(), list():
            for from_first, from_second in zip(first, second):
                diff = compare_pairs(from_first, from_second)
                if diff != 0:
                    return diff
            return compare_pairs(len(first), len(second))
    return 0

# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def _format_dataset(dataset: "list[str]"):
    pairs: list[tuple] = []
    prev = None
    for i, line in enumerate(dataset):
        if i % 2 == 0:
            prev = loads(line)
        else:
            pairs.append((prev, loads(line)))

    return pairs


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

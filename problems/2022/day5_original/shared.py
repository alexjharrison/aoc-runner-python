import pathlib
from os import getenv
from dataclasses import dataclass


@dataclass
class Instructions():
    move: int
    current: int
    to: int

# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def _format_dataset(dataset: "list[str]"):
    num_buckets = 0
    split = 0
    for i, line in enumerate(dataset):
        if len(line) > 0 and line[1].isdigit():
            num_buckets = int(line.split(' ')[-2])
            split = i

    buckets: list[list[str]] = [[] for i in range(num_buckets)]
    for i in range(split - 1, -1, -1):
        line = dataset[i]
        for j in range(num_buckets):
            letter = line[1 + 4 * j]
            if letter != " ":
                buckets[j].append(letter)
            pass

    instructions: list[Instructions] = []
    for line in dataset[split + 2:]:
        a, b, c = line.replace("move ", ",").replace(
            " from ", ",").replace(" to ", ",").split(",")[1:]
        instructions.append(Instructions(
            move=int(a), current=int(b), to=int(c)))
    return (buckets, instructions)


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

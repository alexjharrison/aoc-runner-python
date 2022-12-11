import pathlib
from os import getenv
from dataclasses import dataclass
from typing import Optional


@dataclass
class Assignment():
    a1: int
    a2: int
    b1: int
    b2: int


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    pairs: list[Assignment] = []
    for line in dataset:
        first_pair, second_pair = line.split(",")
        a1, a2 = first_pair.split('-')
        b1, b2 = second_pair.split('-')
        pairs.append(Assignment(
            a1=int(a1),
            a2=int(a2),
            b1=int(b1),
            b2=int(b2),
        ))
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

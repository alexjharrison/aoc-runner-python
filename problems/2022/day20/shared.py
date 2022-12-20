import pathlib
from os import getenv
from dataclasses import dataclass


@dataclass
class Slot:
    value: int

    def __str__(self):
        return str(self.value) + " "

# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def _format_dataset(dataset: "list[str]"):
    return [Slot(int(val)) for val in dataset]


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

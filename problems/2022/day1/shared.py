import pathlib
from os import getenv


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    elves: list[list[int]] = [[]]
    for line in dataset:
        if line != "":
            elves[-1].append(int(line))
        else:
            elves.append([])
    return elves


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

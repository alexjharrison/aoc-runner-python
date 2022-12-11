import pathlib
from os import getenv


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def _format_dataset(dataset: list[str]):
    front_half, back_half = dataset
    print(front_half)

    stacks = [[row[1+(col * 4)] for row in [line for line in front_half.split("\n")][-2::-1]
               if row[1+(col * 4)] != " "] for col in range(int(max(front_half.split('\n')[-1])))]

    directions = [[int(i) for i in line.split() if i.isdigit()]
                  for line in back_half.strip().split("\n")]
    return (stacks, directions)


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = d.read().split("\n\n")
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)


if (__name__ == '__main__'):
    get_dataset()
# rows = [line for line in front_half.split("\n")][-2::-1]
# cols = int(max(front_half.split('\n')[-1]))
# stacks = [[row[1+(col * 4)] for row in rows if row[1+(col * 4)] != " "]
#           for col in range(cols)]

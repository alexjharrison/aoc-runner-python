import pathlib
from os import getenv


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    games: list[int] = []
    for line in dataset:
        them, me = line.split(" ")
        # score = scores[me]
        # score += game_score(scores[them], scores[me])
        score = game_score(scores[them], scores[me])
        print(score)
        games.append(score)
    return games


scores = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3,  # scissors
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}


# rock beats scissors    1 -> 3
# scissors beats paper   3 -> 2
# paper beats rock       2 -> 1

# def game_score(them: int, me: int) -> int:
#     if them == me:
#         return 3
#     if me - them in [-2, 1]:
#         return 6
#     return 0

def game_score(them: int, me: int) -> int:
    my_score = them - 1
    if (my_score == 0):
        my_score = 3

    # i lose
    if me == 1:
        my_score = them - 1
        if (my_score == 0):
            my_score = 3
        return my_score

    # i draw
    if me == 2:
        return them + 3

    # i win
    if me == 3:
        my_score = them + 1
        if (my_score == 4):
            my_score = 1
        return my_score + 6

    return 0


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

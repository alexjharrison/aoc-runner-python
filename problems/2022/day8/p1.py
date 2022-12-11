from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "21"

Coord = set[tuple[int, int]]

# (y,x)


def num_visible_from_left(row_idx: int, row: str) -> Coord:
    matches = set()
    highest = -1
    for col_idx, char in enumerate(row):
        num = int(char)
        coords = (row_idx, col_idx)
        if num > highest:
            matches.add(coords)
            highest = num

    return matches


def num_visible_from_right(row_idx: int, row: str) -> Coord:
    matches = set()
    highest = -1
    for col_idx, char in enumerate(row[::-1]):
        num = int(char)
        coords = (row_idx, len(row) - col_idx - 1)
        if num > highest:
            matches.add(coords)
            highest = num

    return matches


def num_visible_from_top(col_idx: int, col: str) -> Coord:
    matches = set()
    highest = -1
    for row_idx, char in enumerate(col):
        num = int(char)
        coords = (row_idx, col_idx)
        if num > highest:
            matches.add(coords)
            highest = num

    return matches


def num_visible_from_bottom(col_idx: int, col: str) -> Coord:
    matches = set()
    highest = -1
    for row_idx, char in enumerate(col[::-1]):
        num = int(char)
        coords = (len(col) - row_idx - 1, col_idx)
        if num > highest:
            matches.add(coords)
            highest = num

    return matches


def p1() -> str:
    # Solve code here, return string to submit
    visible_points: Coord = set()
    for row_idx, row in enumerate(dataset):
        visible_points = visible_points.union(
            num_visible_from_left(row_idx, row))
        visible_points = visible_points.union(
            num_visible_from_right(row_idx, row))

    for col_idx in range(len(dataset)):
        col = "".join([row[col_idx] for row in dataset])
        visible_points = visible_points.union(
            num_visible_from_top(col_idx, col))
        visible_points = visible_points.union(
            num_visible_from_bottom(col_idx, col))
    grid = [["o" for x in range(len(dataset[0]))] for y in range(len(dataset))]
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            print("X" if (row_idx, col_idx)
                  in visible_points else char, end="")
        print()
    return str(len(visible_points))


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)

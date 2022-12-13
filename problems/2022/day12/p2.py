from shared import get_dataset, shortest_path_distance
from os import getenv
from copy import deepcopy

grid, S, E, height, width = get_dataset()
p2_test_case_answer: str = "29"


def p2() -> str:
    for _, location in enumerate(grid):
        node = grid[location]
        x, y = location
        # check up
        if y > 0:
            neighbor = grid[x, y - 1]
            if neighbor.value - node.value <= 1:
                node.neighbors.append(neighbor)
        # check left
        if x > 0:
            neighbor = grid[x - 1, y]
            if neighbor.value - node.value <= 1:
                node.neighbors.append(neighbor)
        # check down
        if y < height - 1:
            neighbor = grid[x, y + 1]
            if neighbor.value - node.value <= 1:
                node.neighbors.append(neighbor)
        # check right
        if x < width - 1:
            neighbor = grid[x + 1, y]
            if neighbor.value - node.value <= 1:
                node.neighbors.append(neighbor)

    spd = width * height
    for start in grid:
        for node in grid:
            grid[node].visited = False

        if grid[start].value == 0:
            distance = shortest_path_distance(grid[start], grid[E])
            spd = min(spd, distance)

    return str(spd)


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {'nothing' if p2_answer=='' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)

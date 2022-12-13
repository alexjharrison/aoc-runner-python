from shared import get_dataset, shortest_path_distance
from os import getenv


grid, S, E, height, width = get_dataset()
p1_test_case_answer: str = "31"


def p1() -> str:
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
        node.neighbors.sort(
            key=lambda neighbor: neighbor.value, reverse=True)

    spd = shortest_path_distance(grid[S], grid[E])

    return str(spd)


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

from shared import get_dataset
from os import getenv
from itertools import cycle

obstacles = get_dataset()
p2_test_case_answer: str = "93"


def p2() -> str:
    global obstacles
    min_x = min(pt[0] for pt in obstacles) - 1000
    max_x = min(pt[0] for pt in obstacles) + 1000
    floor_y = max(pt[1] for pt in obstacles) + 2
    floor = set(zip(range(min_x, max_x + 1), cycle([floor_y])))
    obstacles |= floor
    units_of_sand = 0
    sand_x = 500
    sand_y = 0
    count = 0
    while (500, 0) not in obstacles:
        if (sand_x, sand_y + 1) not in obstacles:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in obstacles:
            sand_y += 1
            sand_x -= 1
        elif (sand_x + 1, sand_y + 1) not in obstacles:
            sand_y += 1
            sand_x += 1
        else:
            obstacles.add((sand_x, sand_y))
            print(sand_x, sand_y)
            sand_x = 500
            sand_y = 0
            units_of_sand += 1

    return str(units_of_sand)


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

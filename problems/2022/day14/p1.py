from shared import get_dataset
from os import getenv

obstacles = get_dataset()
p1_test_case_answer: str = "24"


def p1() -> str:
    target_y = max(pt[1] for pt in obstacles) + 1
    units_of_sand = 0
    sand_x = 500
    sand_y = 0
    while sand_y < target_y:
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
            sand_x = 500
            sand_y = 0
            units_of_sand += 1
    return str(units_of_sand)


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

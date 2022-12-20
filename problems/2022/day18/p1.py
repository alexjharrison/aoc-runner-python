from shared import get_dataset
from os import getenv

cubes = list(get_dataset())
p1_test_case_answer: str = "64"


def p1() -> str:
    # Solve code here, return string to submit
    # print(cubes)
    total_sides = 6 * len(cubes)

    for i in range(len(cubes)):
        x1, y1, z1 = cubes[i]
        for j in range(len(cubes)):
            x2, y2, z2 = cubes[j]
            if (x1 == x2 and y1 == y2 and abs(z2 - z1) == 1) or (x1 == x2 and z1 == z2 and abs(y2 - y1) == 1) or (z1 == z2 and y1 == y2 and abs(x2 - x1) == 1):
                total_sides -= 1
    return str(total_sides)


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

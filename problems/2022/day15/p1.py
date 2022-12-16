from shared import get_dataset
from os import getenv

pts = get_dataset()
p1_test_case_answer: str = "26"


def p1() -> str:
    beacons = set([pt.b for pt in pts])
    possible_locations = set()
    for pt in pts:
        possible_locations |= pt.range_at_line(2000000)

    return str(len(possible_locations - beacons))


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

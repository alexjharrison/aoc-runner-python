from shared import get_dataset, Slot
from os import getenv
import math


dataset = get_dataset()
p1_test_case_answer: str = "3"


def find_zero_idx(lst: list[Slot]) -> int:
    for i, item in enumerate(lst):
        if item.value == 0:
            return i
    return -1


def prt_arr(list: list[Slot]):
    for item in list:
        print(f"{item.value} ", end="")
    print()


def p1() -> str:
    copy = [x for x in dataset]
    shifted = [x for x in dataset]

    for val in copy:
        shift_val = val.value
        location = shifted.index(val)
        # (location + shift_val) % (len(copy) - 1)
        new_location = int(math.remainder(location + shift_val, len(copy) - 1))

        old_val = shifted.pop(location)
        shifted.insert(new_location, old_val)
        # print(location, new_location, old_val.value)
        # prt_arr(shifted)

    zero_idx = find_zero_idx(shifted)
    # print(shifted[(zero_idx + 1000) % len(shifted)].value, shifted[(zero_idx + 2000) %
    #       len(shifted)].value, shifted[(zero_idx + 3000) % len(shifted)].value)
    sum = 0

    return str(shifted[(zero_idx + 1000) % len(shifted)].value + shifted[(zero_idx + 2000) % len(shifted)].value + shifted[(zero_idx + 3000) % len(shifted)].value)


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

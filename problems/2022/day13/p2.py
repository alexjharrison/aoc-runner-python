from shared import get_dataset, compare_pairs
from os import getenv
import functools


pairs = get_dataset()
p2_test_case_answer: str = "140"


def p2() -> str:
    packets = [[[2]], [[6]]]
    for first, second in pairs:
        packets.append(first)
        packets.append(second)

    packets = sorted(packets, key=functools.cmp_to_key(
        compare_pairs), reverse=True)

    idx2 = packets.index([[2]]) + 1
    idx6 = packets.index([[6]]) + 1
    print(idx2, idx6)
    return str(idx2 * idx6)


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

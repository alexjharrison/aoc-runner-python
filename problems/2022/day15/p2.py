from shared import get_dataset
from os import getenv
from time import time

pts = get_dataset()
p2_test_case_answer: str = "56000011"


def p2() -> str:
    # max_size = 4000000
    max_size = 20
    for row in range(max_size + 1):
        possible_ranges: list[tuple[int, int]] = []
        for pt in pts:
            x1, x2 = pt.range_limits_at_line(row)
            r1 = max(x1, 0)
            r2 = min(x2, max_size + 1)
            possible_ranges.append((r1, r2))
        print(possible_ranges)
        original_ranges = [r for r in possible_ranges]
        prev_len = len(possible_ranges)
        popped_count = 0
        while len(possible_ranges) > 1:
            r1, r2 = possible_ranges[0]
            x1, x2 = possible_ranges[1]
            if x1 > r2 or x2 < r1:
                second = possible_ranges.pop(1)
                possible_ranges.append(second)
                continue
            r1 = x1 if x1 < r1 else r1
            r2 = x2 if x2 > r2 else r2
            possible_ranges.pop(1)
            popped_count += 1
            # possible_ranges[0] = (r1, r2)
            # if possible_ranges[0] == (r1, r2):
            #     possible_ranges.append(second)
            # if possible_ranges[0] == (0, max_size + 1):
            #     break
            print(possible_ranges)
            curr_len = len(possible_ranges)
            if prev_len == curr_len == 2:
                print("found", possible_ranges)
                return str(possible_ranges)
            prev_len = curr_len

    return ""


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

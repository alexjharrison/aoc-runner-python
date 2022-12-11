from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p2() -> str:
    cycles: list[int] = []
    x = 1
    for line in dataset:
        if line == 'noop':
            cycles.append(x)
        else:
            x_addition = int(line.split()[1])
            cycles += [x, x]
            x += x_addition

    output = [" " for _ in range(240)]
    for cycle, curr_x in enumerate(cycles):
        shifted_cycle = cycle % 40
        overlaps = shifted_cycle in [curr_x - 1, curr_x, curr_x + 1]
        output[cycle] = "#" if overlaps else "."

    for row_idx in range(6):
        print("".join(output[row_idx * 40:(row_idx + 1) * 40]))
    return "EKRHEPUZ"


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

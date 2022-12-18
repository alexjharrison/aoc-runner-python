from shared import get_dataset, Grid, Tetronimono
from os import getenv

gas_blasts = get_dataset()
p2_test_case_answer: str = "1514285714288"


def p2() -> str:
    # Solve code here, return string to submit
    grid = Grid()
    iterations = 1_000_000_000_000
    blast_count = 0
    for i in range(iterations):
        tetr = Tetronimono(i, grid)
        while not tetr.has_stopped:
            blast = gas_blasts[blast_count]
            if blast == "<":
                tetr.go_left()
            elif blast == ">":
                tetr.go_right()
            tetr.go_down()
            blast_count = (blast_count + 1) % len(gas_blasts)
            tetr.print()
        # tetr.print()

    return f"{grid.y_max}"


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

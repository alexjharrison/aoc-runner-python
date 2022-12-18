from shared import get_dataset, Grid, Tetronimono
from os import getenv

gas_blasts = get_dataset()
p1_test_case_answer: str = "3068"


def p1() -> str:
    # Solve code here, return string to submit
    grid = Grid()
    iterations = 2022
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
        # tetr.print()

    return f"{grid.y_max}"


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

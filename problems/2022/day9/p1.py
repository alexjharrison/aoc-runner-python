from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "13"


def p1() -> str:
    head_x: int = 0
    head_y: int = 0
    tail_x: int = 0
    tail_y: int = 0
    history_tail: set[tuple[int, int]] = set()

    for line in dataset:
        direction, distance = line.split()
        for _ in range(int(distance)):
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
            dx = head_x - tail_x
            dy = head_y - tail_y

            if abs(dy) == 2 and dx == 0:
                tail_y += 1 if dy > 0 else -1
            elif abs(dx) == 2 and dy == 0:
                tail_x += 1 if dx > 0 else -1
            elif abs(dy) == 2 and abs(dx) == 1:
                tail_y += 1 if dy > 0 else -1
                tail_x += dx
            elif abs(dx) == 2 and abs(dy) == 1:
                tail_x += 1 if dx > 0 else -1
                tail_y += dy

            history_tail.add((tail_x, tail_y))
    return str(len(history_tail))


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

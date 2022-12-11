from shared import get_dataset
from os import getenv, system
from time import sleep
from string import ascii_lowercase

dataset = get_dataset()
p2_test_case_answer: str = "36"


def print_train(train: list[tuple[int, int]], history_tail: set[tuple[int, int]]):
    # print(train)
    width = 30
    height = 22
    for y in range(height - 6, -6, -1):
        for x in range(-width // 2, width // 2):
            print(
                "#" if (x, y) in history_tail else
                ascii_lowercase[train.index((x, y))]
                if (x, y) in train else "_" if y == 0 else "|" if x == 0 else ".", end="")
        print()
    print()


def p2() -> str:
    train: list[tuple[int, int]] = [(0, 0) for i in range(10)]
    history_tail: set[tuple[int, int]] = set()

    for line in dataset:
        direction, distance = line.split()
        for _ in range(int(distance)):
            for knot_idx in range(1, len(train)):
                head_x, head_y = train[knot_idx - 1]
                tail_x, tail_y = train[knot_idx]

                if knot_idx == 1:
                    if direction == 'R':
                        head_x += 1
                    elif direction == 'L':
                        head_x -= 1
                    elif direction == 'U':
                        head_y += 1
                    elif direction == 'D':
                        head_y -= 1
                    train[knot_idx - 1] = (head_x, head_y)

                dx = head_x - tail_x
                dy = head_y - tail_y

                if abs(dy) == 2 and dx == 0:
                    tail_y += 1 if dy > 0 else -1
                elif abs(dx) == 2 and dy == 0:
                    tail_x += 1 if dx > 0 else -1
                elif abs(dy) == 2 and abs(dx) == 1:
                    tail_y += 1 if dy > 0 else -1
                    tail_x += 1 if dx > 0 else -1
                elif abs(dx) == 2 and abs(dy) == 1:
                    tail_x += 1 if dx > 0 else -1
                    tail_y += 1 if dy > 0 else -1
                elif abs(dx) == 2 == abs(dy):
                    tail_y += 1 if dy > 0 else -1
                    tail_x += 1 if dx > 0 else -1

                train[knot_idx] = (tail_x, tail_y)

                if knot_idx == len(train) - 1:
                    history_tail.add((tail_x, tail_y))
                system("clear")
                print_train(train, history_tail)
                sleep(.01)
    return str(len(history_tail))


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

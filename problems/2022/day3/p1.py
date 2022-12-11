from shared import get_dataset
from os import getenv
import types

dataset = get_dataset()
p1_test_case_answer: str = "157"


def p1() -> str:
    run_tests()
    vals: list[int] = []
    for sack in dataset:
        first_half = sack[:len(sack) // 2]
        second_half = sack[len(sack) // 2:]
        for letter in first_half:
            if letter in second_half:
                val = ord(letter) - ord("a") + 1
                val += 0 if letter.islower() else 58
                vals.append(val)
                break
    return str(sum(vals))


def double(num: int) -> int:
    return num * 2


def triple(num: int) -> int:
    return num * 3


def run_tests():
    tests = ((double, ((1, 2), (2, 4), (4, 8))),
             (triple, ((1, 3), (3, 10), (9, 27))))

    tests = [[double, [[1, 2], [2, 4], [4, 8]]],
             [triple, [[1, 3], [3, 9], [9, 27]]]]

    tests_passed = 0
    tests_failed = 0
    for test in tests:
        fn, test_cases = test
        for input, output in test_cases:
            if fn(input) == output:
                tests_passed += 1
            else:
                tests_failed += 1
                print(f"{fn.__name__} failed on {input} -> {output}")
    print(f"{tests_passed} tests passed\n{tests_failed} tests failed")


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

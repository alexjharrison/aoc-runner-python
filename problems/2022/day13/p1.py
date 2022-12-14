from shared import get_dataset, compare_pairs
from os import getenv

pairs = get_dataset()
p1_test_case_answer: str = "13"


def p1() -> str:
    # Solve code here, return string to submit
    true_pairs = sum([i+1 for i, pair in enumerate(
        pairs) if compare_pairs(pair[0], pair[1]) > 0])
    return str(true_pairs)


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
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "19"


def p2() -> str:
    for i in range(len(dataset)):
        four_set = dataset[i:i+14]
        this_set = set(four_set)
        if len(four_set) == len(this_set):
            return str(i + 14)
    return "NOT FOUND"


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

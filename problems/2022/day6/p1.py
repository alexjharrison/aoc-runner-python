from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "7"


def p1() -> str:
    for i in range(len(dataset)):
        four_set = dataset[i:i+4]
        this_set = set(four_set)
        if len(four_set) == len(this_set):
            return str(i + 4)
    return "NOT FOUND"


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

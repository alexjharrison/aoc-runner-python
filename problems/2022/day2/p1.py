from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "15"


def p1() -> str:
    dictionary = {
        "A X": 3 + 1,
        "A Y": 6 + 2,
        "A Z": 0 + 3,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 6 + 1,
        "C Y": 0 + 2,
        "C Z": 3 + 3,
    }
    return str(sum([dictionary[game] for game in dataset]))


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

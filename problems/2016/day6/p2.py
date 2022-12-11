from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "advent"


def p2() -> str:
    hash: list[dict[str, int]] = [dict() for _ in dataset[0]]
    for line in dataset:
        for col, letter in enumerate(line):
            if letter in hash[col]:
                hash[col][letter] += 1
            else:
                hash[col][letter] = 1
    answer = ""
    for col in hash:
        min = 10000
        min_letter = ""
        for letter, count in col.items():
            if count < min:
                min = count
                min_letter = letter
        answer += min_letter

    return answer


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

from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "easter"


def p1() -> str:
    # Solve code here, return string to submit
    hash: list[dict[str, int]] = [dict() for _ in dataset[0]]
    for line in dataset:
        for col, letter in enumerate(line):
            if letter in hash[col]:
                hash[col][letter] += 1
            else:
                hash[col][letter] = 1
    answer = ""
    for col in hash:
        max = 0
        max_letter = ""
        for letter, count in col.items():
            if count > max:
                max = count
                max_letter = letter
        answer += max_letter

    return answer


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

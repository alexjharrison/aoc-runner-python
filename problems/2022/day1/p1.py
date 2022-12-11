from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "24000"


def p1() -> str:
    # Solve code here, return string to submit
    max_elf = 0
    for elf in dataset:
        elf_count = 0
        for food_item in elf:
            elf_count += food_item
        max_elf = max(elf_count, max_elf)
    return str(max_elf)


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

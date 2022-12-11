from shared import get_dataset, Folder
from os import getenv

p1_test_case_answer: str = "95437"

total = 0


def get_folder_sizes(tree: Folder):
    global total
    folder_size = tree.get_size()
    if folder_size <= 100000:
        total += folder_size
    for directory in tree.directories.values():
        get_folder_sizes(directory)


def p1() -> str:
    # Solve code here, return string to submit

    tree = get_dataset()
    get_folder_sizes(tree)
    return str(total)


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

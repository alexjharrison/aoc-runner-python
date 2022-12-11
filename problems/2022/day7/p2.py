from shared import get_dataset, Folder
from os import getenv

tree = get_dataset()
p2_test_case_answer: str = "24933642"
total_size = tree.get_size()
unused_space = 0  # 70_000_000 - tree.get_size()
deleted_folder_size = 70_000_000


def get_folder_sizes(branch: Folder):
    global deleted_folder_size
    branch_size = branch.get_size()
    if total_size - branch_size < 40_000_000:
        print(branch_size)
        deleted_folder_size = min(branch_size, deleted_folder_size)
    for directory in branch.directories.values():
        get_folder_sizes(directory)


def p2() -> str:
    get_folder_sizes(tree)
    print(tree)
    return str(deleted_folder_size)


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

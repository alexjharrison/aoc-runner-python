from shared import get_dataset
from os import getenv

monkeys = get_dataset(True)
p2_test_case_answer: str = "2713310158"


def p2() -> str:
    for round in range(10000):
        for monke in monkeys:
            while len(monke.items) > 0:
                monke_target, item = monke.inspect()
                monkeys[monke_target].add_item(item)
    inspections = sorted([monke.inspection_count for monke in monkeys])
    return str(inspections[-1] * inspections[-2])


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

import pathlib
from os import getenv
from re import findall
from collections.abc import Callable

voodoo = r'\d+'
fear_reducer = 3
lcm = 1


def add_by(val: int):
    def higher_order_add(val2: int):
        return val2 + val
    return higher_order_add


def multiply_by(val: int):
    def higher_order_multiply(val2: int):
        return val2 * val
    return higher_order_multiply


def square(val: int):
    return val ** 2


class Monkey:
    def __init__(self, operation: Callable[[int], int],
                 items: list[int],
                 divisible_test_num: int,
                 test_true_monkey_idx: int,
                 test_false_monkey_idx: int,
                 inspection_count: int = 0) -> None:
        global lcm
        self.operation = operation
        self.items = items
        self.divisible_test_num = divisible_test_num
        self.test_true_monkey_idx = test_true_monkey_idx
        self.test_false_monkey_idx = test_false_monkey_idx
        self.inspection_count = inspection_count
        lcm *= divisible_test_num

    # returns (monkey_idx, item)
    def inspect(self) -> tuple[int, int]:
        self.inspection_count += 1
        item = self.items[0]
        self.items = self.items[1:]
        new_worry_level = (self.operation(item) // fear_reducer) % lcm
        return (self.test_true_monkey_idx
                if new_worry_level % self.divisible_test_num == 0
                else self.test_false_monkey_idx,
                new_worry_level)

    def add_item(self, item: int):
        self.items.append(item)

    def __str__(self) -> str:
        return str(self.inspection_count)


def _format_dataset(dataset: str) -> list[Monkey]:
    monkey_data = dataset.split('\n\n')
    monkeys: list[Monkey] = []
    for monkey in monkey_data:
        monkey_line = monkey.split('\n')
        items = [int(num) for num in findall(voodoo, monkey_line[1])]
        divisible_test_num = int(findall(voodoo, monkey_line[3])[0])
        test_true_monkey_idx = int(monkey_line[4][-1])
        test_false_monkey_idx = int(monkey_line[5][-1])

        if "* old" in monkey_line[2]:
            monkeys.append(Monkey(square, items, divisible_test_num,
                                  test_true_monkey_idx, test_false_monkey_idx))
        elif "*" in monkey_line[2]:
            multiplicant = int(findall(voodoo, monkey_line[2])[0])
            monkeys.append(Monkey(multiply_by(multiplicant), items, divisible_test_num,
                                  test_true_monkey_idx, test_false_monkey_idx))
        elif "+" in monkey_line[2]:
            addicant = int(findall(voodoo, monkey_line[2])[0])
            monkeys.append(Monkey(add_by(addicant), items, divisible_test_num,
                                  test_true_monkey_idx, test_false_monkey_idx))
    return monkeys


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset(is_terrified=False):
    global fear_reducer
    fear_reducer = 1 if is_terrified else 3
    with open(folder + file, 'r') as d:
        lines = d.read()
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

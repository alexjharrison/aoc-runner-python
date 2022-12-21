import pathlib
from os import getenv
from typing import Optional, Callable


def add(a: int, b: int):
    return a + b


def sub(a: int, b: int):
    return a - b


def mult(a: int, b: int):
    return a * b


def div(a: int, b: int):
    return a // b


monkes: dict[str, "Monke"] = {}


class Monke:
    def __init__(self, name: str, val: Optional[int], op: Optional[Callable[[int, int], int]],  mother: Optional[str], father: Optional[str]):
        self.name = name
        self.val = val
        self.mother = mother
        self.father = father
        self.op = op

    def get_val(self) -> int:
        if self.val:
            return self.val
        elif self.mother and self.father and self.op:
            self.val = self.op(
                monkes[self.mother].get_val(), monkes[self.father].get_val())
            return self.val
        else:
            return -1000000


def _format_dataset(dataset: "list[str]"):
    for monke in dataset:
        name, op_or_val = monke.split(": ")
        if op_or_val[0].isnumeric():
            monkes[name] = Monke(name, int(op_or_val), None, None, None)
        elif op_or_val[5] == "+":
            mother, father = op_or_val.split(" + ")
            monkes[name] = Monke(name, None, add, mother, father)
        elif op_or_val[5] == "-":
            mother, father = op_or_val.split(" - ")
            monkes[name] = Monke(name, None, sub, mother, father)
        elif op_or_val[5] == "*":
            mother, father = op_or_val.split(" * ")
            monkes[name] = Monke(name, None, mult, mother, father)
        elif op_or_val[5] == "/":
            mother, father = op_or_val.split(" / ")
            monkes[name] = Monke(name, None, div, mother, father)
    for monke in monkes:
        monkes[monke].get_val()
    return monkes


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

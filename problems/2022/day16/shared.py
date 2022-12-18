import pathlib
from os import getenv
from queue import Queue
from functools import cmp_to_key


class Valve:
    def __init__(self, name: str, flow_rate: int) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.is_closed = True
        self.children: list[Valve] = []
        self.distance_to: dict[str, int] = {self.name: 0}

    def __str__(self) -> str:
        return f"""
        Valve {self.name}: {self.flow_rate}
        Children: {[child.name for child in self.children]}
        Distances: {", ".join([f"{target}:{dist}" for target,dist in self.distance_to.items()])}
        """

    def get_target_potential(self, target_name: str, time: int):
        return self.flow_rate * (time - self.distance_to[target_name] - 1)


def nodes_with_unopened_valves(valves: dict[str, Valve]) -> list[Valve]:
    return [valve for valve in valves.values() if valve.is_closed and valve.flow_rate > 0]


def get_best_target(time: int, origin: Valve, targets: list[Valve]) -> Valve:
    potentials = [valve.get_target_potential(
        origin.name, time) for valve in targets]
    max_potential = max(potentials)

    print(max_potential, potentials.index(max_potential), potentials)

    return targets[potentials.index(max_potential)]


def reset_valves(valves: dict[str, Valve]) -> None:
    for valve in valves.values():
        valve.is_closed = True


def calc_distance(origin: Valve, target: Valve) -> None:
    if (target.name in origin.distance_to):
        return
    visited: set[str] = set(origin.name)
    q: Queue[tuple[int, Valve]] = Queue()
    q.put((0, origin))
    while True:
        level, curr = q.get()

        if curr.name in visited:
            continue
        visited.add(curr.name)

        if curr == target:
            origin.distance_to[target.name] = level
            target.distance_to[origin.name] = level
            return
        for child in curr.children:
            q.put((level + 1, child))


def _format_dataset(dataset: "list[str]"):
    valves: dict[str, Valve] = {}
    child_map: dict[str, list[str]] = {}
    for line in dataset:
        line = line.replace("=", " ").replace(
            ";", "").replace(",", "", 5).split(" ")
        valves[line[1]] = Valve(line[1], int(line[5]))
        child_map[line[1]] = line[10:]
    for parent in child_map:
        valves[parent].children = [valves[child]
                                   for child in child_map[parent]]

    for origin in valves.values():
        for target in valves.values():
            calc_distance(origin, target)

    return valves


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

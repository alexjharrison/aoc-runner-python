from shared import get_dataset, Valve, nodes_with_unopened_valves, get_best_target
from os import getenv


valves = get_dataset()
p1_test_case_answer: str = "1651"


def p1() -> str:
    cum_pressure = 0
    path: list[Valve] = [valves["AA"]]
    t = 30
    while t > 0:
        current_location = path[-1]
        # possible_targets = nodes_with_unopened_valves(valves)
        possible_targets = [valves["DD"], valves["BB"],
                            valves["JJ"], valves["HH"], valves["EE"], valves["CC"]][len(path) - 1:]
        print("\ntarget", end=": ")
        for target in possible_targets:
            print(target.name, end=", ")
        print("\npath", end=": ")
        for path_item in path:
            print(path_item.name, end=", ")
        print()

        best_target = current_location

        if len(possible_targets) > 0:
            # best_target = get_best_target(
            #     t, current_location, possible_targets)
            best_target = possible_targets[0]

        for tick in range(current_location.distance_to[best_target.name] + 1):
            previous_flows = [valve.flow_rate for valve in path]
            pressure_per_tick = sum(previous_flows)

            cum_pressure += pressure_per_tick
            print("\ntime: ", t)
            print("Pressure per tick: ", pressure_per_tick)
            print("cum pressure", cum_pressure)
            t -= 1
            if t < 0:
                return str(cum_pressure)
        best_target.is_closed = False
        if best_target != current_location:
            path.append(best_target)

    return str(cum_pressure)


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

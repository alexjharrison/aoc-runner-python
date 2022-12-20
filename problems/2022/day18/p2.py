from shared import get_dataset
from os import getenv

cubes = get_dataset()
p2_test_case_answer: str = "58"

Point = tuple[int, int, int]
cube_min = -1
cube_max = 23


def fall(pt_to_check: Point, falling_plane_index: int, going_up: bool, water_pts: set[Point] = set()):
    # out of bounds
    if min(pt_to_check) < cube_min or max(pt_to_check) > cube_max:
        return water_pts

    # already checked
    if pt_to_check in water_pts or pt_to_check in cubes:
        return water_pts

    water_pts.add(pt_to_check)

    axis_1 = (falling_plane_index + 1) % 3
    axis_2 = (falling_plane_index + 2) % 3

    # fall down
    under = list(pt_to_check)
    under[falling_plane_index] += 1 if going_up else -1
    fall(tuple(under), falling_plane_index, going_up, water_pts)

    # spread
    ahead = list(pt_to_check)
    ahead[axis_1] += 1
    fall(tuple(ahead), falling_plane_index, going_up, water_pts)

    behind = list(pt_to_check)
    behind[axis_1] -= 1
    fall(tuple(behind), falling_plane_index, going_up, water_pts)

    left = list(pt_to_check)
    left[axis_2] += 1
    fall(tuple(left), falling_plane_index, going_up, water_pts)

    right = list(pt_to_check)
    right[axis_2] -= 1
    fall(tuple(right), falling_plane_index, going_up, water_pts)

    return water_pts


def p2() -> str:
    all_water_pts: set[Point] = set()
    for axis_1 in range(cube_min, cube_max):
        for axis_2 in range(cube_min, cube_max):
            # fall from z max
            all_water_pts |= fall((axis_1, axis_2, cube_max), 2, False)
            # fall from z min
            all_water_pts |= fall((axis_1, axis_2, cube_min), 2, True)
            # fall from y max
            all_water_pts |= fall((axis_1, cube_max, axis_2), 1, False)
            # fall from y min
            all_water_pts |= fall((axis_1, cube_min, axis_2), 1, True)
            # fall from x max
            all_water_pts |= fall((cube_max, axis_1, axis_2), 0, False)
            # fall from x min
            all_water_pts |= fall((cube_min, axis_1, axis_2), 0, True)

    print(len(all_water_pts))
    print(len(cubes))
    print(len(cubes) + len(all_water_pts))
    # print(all_water_pts)
    print((cube_max - cube_min + 1) ** 3)
    print((2, 2, 5) not in all_water_pts | cubes)

    num_sides = 0
    cube_list = list(cubes)
    for i in range(len(cube_list)):
        x, y, z = cube_list[i]

        for offset in [-1, 1]:
            if (x + offset, y, z) in all_water_pts:
                num_sides += 1
            if (x, y + offset, z) in all_water_pts:
                num_sides += 1
            if (x, y, z + offset) in all_water_pts:
                num_sides += 1
    return str(num_sides)


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

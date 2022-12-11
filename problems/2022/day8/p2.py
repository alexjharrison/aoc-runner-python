from shared import get_dataset
from os import getenv
from grid import Grid

dataset = get_dataset()
p2_test_case_answer: str = "8"


Coord = set[tuple[int, int]]


def p2() -> str:
    # Solve code here, return string to submit
    best_tree_score = 0
    grid = Grid(dataset)
    for y, row in enumerate(grid.points):
        for x, pt in enumerate(row):
            curr_tree_score: list[int] = [0, 0, 0, 0]
        # check left
            curr_x, curr_y = x, y
            while True:
                left = grid.get_left(curr_x, curr_y)
                if not left:
                    break
                curr_x, curr_y, left_val = left.x, left.y, left.val
                curr_tree_score[0] += 1
                if left.val >= pt.val:
                    break
        # check right
            curr_x, curr_y = x, y
            while True:
                right = grid.get_right(curr_x, curr_y)
                if not right:
                    break
                curr_x, curr_y, right_val = right.x, right.y, right.val
                curr_tree_score[1] += 1
                if right.val >= pt.val:
                    break
        # check above
            curr_x, curr_y = x, y
            while True:
                above = grid.get_above(curr_x, curr_y)
                if not above:
                    break
                curr_x, curr_y, above_val = above.x, above.y, above.val
                curr_tree_score[2] += 1
                if above.val >= pt.val:
                    break
        # check below
            curr_x, curr_y = x, y
            while True:
                below = grid.get_below(curr_x, curr_y)
                if not below:
                    break
                curr_x, curr_y, below_val = below.x, below.y, below.val
                curr_tree_score[3] += 1
                if below.val >= pt.val:
                    break
            best_tree_score = max(
                curr_tree_score[0] * curr_tree_score[1] * curr_tree_score[2] * curr_tree_score[3], best_tree_score)
            print(str(curr_tree_score) +
                  ((3 - len(str(curr_tree_score))) * " "), end="")
        print()

    return str(best_tree_score)


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

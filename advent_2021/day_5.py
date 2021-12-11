def read_inputs(input_file):
    vent_positions = []
    with open(input_file) as f:
        for line in f:
            position = []
            for coordinate in line.strip().split(" -> "):
                position.append(
                    tuple([int(val) for val in coordinate.split(",")])
                )
            vent_positions.append(position)
    return vent_positions


def get_vent_grid(vent_positions, include_diagonal):
    vent_grid = {}
    for position in vent_positions:
        (x1, y1), (x2, y2) = position
        if x1 == x2 and y1 == y2:
            vent_grid[x1 + "__" + y1] = vent_grid.get(x1 + "__" + y1, 0) + 1
            continue
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    vent_grid[(x1, y)] = vent_grid.get((x1, y), 0) + 1
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    vent_grid[(x, y1)] = vent_grid.get((x, y1), 0) + 1
        if include_diagonal and x1 != x2 and y1 != y2:
            if x1 < x2:
                x_step = 1
                x_end = x2 + 1
            elif x1 > x2:
                x_step = -1
                x_end = x2 - 1
            if y1 < y2:
                y_step = 1
                y_end = y2 + 1
            elif y1 > y2:
                y_step = -1
                y_end = y2 - 1
            for x, y in zip(
                range(x1, x_end, x_step),
                range(y1, y_end, y_step),
            ):
                vent_grid[(x, y)] = vent_grid.get((x, y), 0) + 1

    return vent_grid


def count_overlap_lines(vent_grid, min_overlap=2):
    overlap_count = 0
    for k, v in vent_grid.items():
        if v >= 2:
            overlap_count += 1
    return overlap_count


def compute_overlap_lines(
    input_file,
    min_overlap,
    include_diagonal,
):
    vent_positions = read_inputs(input_file)
    vent_grid = get_vent_grid(
        vent_positions,
        include_diagonal,
    )
    return count_overlap_lines(vent_grid, min_overlap)


if __name__ == "__main__":
    assert (
        compute_overlap_lines(
            input_file="inputs/test_day_5_input.txt",
            min_overlap=2,
            include_diagonal=False,
        )
        == 5
    )
    print(
        compute_overlap_lines(
            input_file="inputs/day_5_input.txt",
            min_overlap=2,
            include_diagonal=False,
        )
    )
    assert (
        compute_overlap_lines(
            input_file="inputs/test_day_5_input.txt",
            min_overlap=2,
            include_diagonal=True,
        )
        == 12
    )
    print(
        compute_overlap_lines(
            input_file="inputs/day_5_input.txt",
            min_overlap=2,
            include_diagonal=True,
        )
    )
